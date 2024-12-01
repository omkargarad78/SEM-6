import java.nio.ByteBuffer;
import java.nio.ByteOrder;

public class MD5Example {
    private static final int BLOCK_SIZE = 64; // 512 bits
    private static final int DIGEST_LENGTH = 16; // 128 bits

    public static void main(String[] args) {
        String text = "Hello, world my name is Omkar";
        byte[] md5Hash = calculateMD5(text.getBytes());
        System.out.println("MD5 hash of '" + text + "': " + bytesToHex(md5Hash));
    }

    public static byte[] calculateMD5(byte[] input) {
        int[] state = { 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476 };
        int[] K = new int[64];
        for (int i = 0; i < 64; i++) {
            K[i] = (int) (Math.floor(Math.abs(Math.sin(i + 1)) * (1L << 32)));
        }
        int[] s = {
            7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
            5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
            4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
            6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
        };
        byte[] paddedInput = padMessage(input);
        byte[][] chunks = splitIntoChunks(paddedInput, BLOCK_SIZE);
        for (byte[] chunk : chunks) {
            int[] words = splitIntoWords(chunk, 4);
            int A = state[0], B = state[1], C = state[2], D = state[3];
            for (int i = 0; i < 64; i++) {
                int F, g;
                if (i < 16) {
                    F = (B & C) | (~B & D);
                    g = i;
                } else if (i < 32) {
                    F = (D & B) | (~D & C);
                    g = (5 * i + 1) % 16;
                } else if (i < 48) {
                    F = B ^ C ^ D;
                    g = (3 * i + 5) % 16;
                } else {
                    F = C ^ (B | ~D);
                    g = (7 * i) % 16;
                }
                int temp = D;
                D = C;
                C = B;
                B = B + rotateLeft(A + F + K[i] + words[g], s[i]);
                A = temp;
            }
            state[0] += A;
            state[1] += B;
            state[2] += C;
            state[3] += D;
        }
        return intArrayToByteArray(state);
    }

    private static byte[] padMessage(byte[] input) {
        int len = input.length;
        int paddedLen = (BLOCK_SIZE - (len % BLOCK_SIZE)) % BLOCK_SIZE;
        int messageLen = len + paddedLen + 8;
        byte[] paddedInput = new byte[messageLen];
        System.arraycopy(input, 0, paddedInput, 0, len);
        paddedInput[len] = (byte) 0x80;
        for (int i = len + 1; i < messageLen - 8; i++) {
            paddedInput[i] = 0;
        }
        long bitLength = (long) len * 8;
        for (int i = 0; i < 8; i++) {
            paddedInput[messageLen - 8 + i] = (byte) ((bitLength >>> (i * 8)) & 0xFF);
        }
        return paddedInput;
    }

    private static byte[][] splitIntoChunks(byte[] input, int chunkSize) {
        int numOfChunks = input.length / chunkSize;
        byte[][] chunks = new byte[numOfChunks][chunkSize];
        for (int i = 0; i < numOfChunks; i++) {
            System.arraycopy(input, i * chunkSize, chunks[i], 0, chunkSize);
        }
        return chunks;
    }

    private static int[] splitIntoWords(byte[] input, int wordSize) {
        int numOfWords = input.length / wordSize;
        int[] words = new int[numOfWords];
        for (int i = 0; i < numOfWords; i++) {
            words[i] = ByteBuffer.wrap(input, i * wordSize, wordSize)
                                .order(ByteOrder.LITTLE_ENDIAN).getInt();
        }
        return words;
    }

    private static int rotateLeft(int x, int n) {
        return (x << n) | (x >>> (32 - n));
    }

    private static byte[] intArrayToByteArray(int[] input) {
        byte[] output = new byte[DIGEST_LENGTH];
        for (int i = 0, j = 0; i < input.length; i++) {
            output[j++] = (byte) (input[i] & 0xFF);
            output[j++] = (byte) ((input[i] >> 8) & 0xFF);
            output[j++] = (byte) ((input[i] >> 16) & 0xFF);
            output[j++] = (byte) ((input[i] >> 24) & 0xFF);
        }
        return output;
    }

    private static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02x", b & 0xff));
        }
        return sb.toString();
    }
}
