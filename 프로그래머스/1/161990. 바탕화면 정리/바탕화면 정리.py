def solution(wallpaper):
    minX, minY, maxX, maxY = int(1e9), int(1e9), 0, 0
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x] == '#':
                minX = min(minX, x)
                minY = min(minY, y)
                maxX = max(maxX, x+1)
                maxY = max(maxY, y+1)
    return [minY, minX, maxY, maxX]
    