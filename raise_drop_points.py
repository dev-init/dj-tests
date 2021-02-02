#!/bin/python

import sys
import time

max_height = 0


def get_max_height(x, points):
    mp = [p for p in points if x == p[0]]
    return max(mp, key=lambda a: a[2])

def get_next_point(lx2, lh, points):
    np = []

    for p in points:
        x1, x2, h = p
        if (x1 < lx2 and x2 < lx2 and h > max_height) or (x1 < lx2 and x2 > lx2): 
            np.append(p)    

    if np:
        raising = [x for x in np if max_height < x[2]]
        if raising:            
            return min(raising, key=lambda a: a[2])
        else:
            return max(np, key=lambda a: a[2])
    else:
        return None

def get_np_after_gap(lx2, points):
    for p in points:        
        if p[0] > lx2:
            return p
    return None

def remove_covered(points):
    i = 0
    while i < len(points):
        ax1, ax2, ah = points[i]
        j = i + 1
        while j < len(points):
            bx1, bx2, bh = points[j]
            if bx1 > ax1 and bx2 < ax2 and bh < ah:
                points.remove((bx1, bx2, bh))
            j += 1
        i += 1
    return points


def main():
    # points = [(1, 5, 10), (4, 6, 8), (10, 15, 10), (11,12,8)] 
    # OP: [(1, 10),(5, 8),(6, 0),(10, 10),(15, 0)]
    # points = [(1, 10, 4),(1, 8, 6),(1, 6, 8)] 
    # OP: [(1, 8),(6, 6),(8, 4),(10, 0)]
    # points = [(0, 6, 2),(5, 10, 8),(7, 8, 12)] 
    # OP: [(0,2), (5, 8),(7, 12),(8, 8) (10, 0)]q
    # points = [(0, 6, 2), (3, 12, 6), (5, 10, 8), (7, 8, 12)] 
    # OP: [(0, 2), (3, 6), (5, 8), (7, 12), (8, 8), (10, 6), (12, 0)]
    # points = [(1, 4, 4), (3, 5, 8), (6, 7, 2), (8, 13, 6), (10, 15, 10)] 
    # OP: [(1, 4), (3, 8), (5, 0), (6, 2), (7, 0), (8, 6), (10, 10), (15, 0)]
    points = [(1, 4, 4), (2, 15, 12), (3, 5, 8), (6, 7, 2), (8, 13, 6), (10, 14, 10)] 
    # OP: [(1, 4), (2, 11), (14, 10), (15, 0)]

    points = remove_covered(points)
    # print(points)
    rd_points = []
    visited = []

    x1, x2, h = points[0]
    p = get_max_height(x1, points)
    rd_points.append((x1, p[2]))
    last_h = p[2]
    last_x2 = p[1]

    global max_height
    if p[2] > max_height:
        max_height = p[2]
    visited.append(p)

    while True:
        p = get_next_point(last_x2, last_h, points)
        if p:             
            if last_x2 > p[0] and last_h < p[2]:
                rd_points.append((p[0], p[2]))
            else:
                rd_points.append((last_x2, p[2]))                            
            last_x2 = p[1]
            last_h = p[2]
            if p[2] > max_height:
                max_height = p[2]                        
        else:
            rd_points.append((last_x2, 0))
            p = get_np_after_gap(last_x2, points)
            for x in visited:
                if points:
                    points.remove(x)
            visited = []
            if p:
                x1, x2, h = p
                p = get_max_height(x1, points)
                rd_points.append((x1, p[2]))
                last_x2 = p[1]
                last_h = p[2]
                if p[2] > max_height:
                    max_height = p[2]                        
            else:
                break
        visited.append(p)
            
    print(rd_points)


if __name__ == '__main__':
    main()
