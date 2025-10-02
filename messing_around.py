expt_samples = []

tokens = input().split()
for token in tokens:
    expt_samples.append(int(token))
print("Original samples:", end=" ")
for samples in expt_samples:
    print(samples, end=" ")
print()
# start
removed = [x for x in expt_samples if x >= 55]
for r in removed:
    print(f"{r} removed")
expt_samples = [x for x in expt_samples if x < 55]
# stop
print("Filtered samples:", end=" ")
for samples in expt_samples:
    print(samples, end=" ")
print()