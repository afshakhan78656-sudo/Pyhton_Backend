def round_views(titles, views):
    result = [(title, round(count, -3)) for title, count in zip(titles, views)]
    return result


titles = ["Python Basics", "Django Tutorial", "Learn SQL"]
views = [4567, 12890, 2345]

print(round_views(titles, views))

