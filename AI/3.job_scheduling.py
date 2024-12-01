n = int(input("Enter the number of jobs: "))
arr = []

for i in range(n):
  job_id = input("\nEnter job id: ")
  duration = int(input("Enter deadline: "))
  profit = int(input("Enter profit: "))
  arr.append([job_id, duration, profit])

print("\nGiven Values :")
for job in arr:
   print(f"\tJob ID: {job[0]}, Deadline: {job[1]}, Profit: {job[2]}")

deadlines =[]
for job in arr:
   deadlines.append(job[1])
t = max(deadlines)

for i in range(n):
  for j in range(n - 1 - i):
      if arr[j][2] < arr[j + 1][2]:
          arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("\nSorted according to Profit:")
for job in arr:
   print(f"\tJob ID: {job[0]}, Deadline: {job[1]}, Profit: {job[2]}")

result = [False] * t
job = ['-1'] * t
total_profit = 0

for i in range(len(arr)):
  for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
      if result[j] is False:
          result[j] = True
          job[j] = arr[i][0]
          total_profit += arr[i][2]
          break
job = [job_id for job_id in job if job_id != '-1']

print("\nJob sequence for maximum profit - {}".format(job))
print("\nTotal Maximum Profit: {} \n".format(total_profit))