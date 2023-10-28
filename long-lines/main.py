n, h0, a, c, q = map(int, input().split())

heights = []
heights.append(h0)

for i in range(1, n):
    new_height = (a * heights[i - 1] + c) % q
    heights.append(new_height)

heights = heights[::-1]

noticable_people = 0

for i in range(0, len(heights) - 1):
    people = []
    people.append(heights[i + 1])
    for j in range(i + 2, len(heights)):
        if heights[j] > people[len(people) - 1]:
            people.append(heights[j])
    noticable_people += len(people)

print(noticable_people)
