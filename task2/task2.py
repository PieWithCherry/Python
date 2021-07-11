import math
import re


def checkPoint(cx, cy, cz, R, PX0, PY0, PZ0, PX1, PY1, PZ1):
    vx = PX1 - PX0
    vy = PY1 - PY0
    vz = PZ1 - PZ0
    A = vx * vx + vy * vy + vz * vz
    B = 2.0 * (PX0 * vx + PY0 * vy + PZ0 * vz - vx * cx - vy * cy - vz * cz)
    C = PX0 * PX0 - 2 * PX0 * cx + cx * cx + PY0 * PY0 - 2 * PY0 * cy + cy * cy + PZ0 * PZ0 - 2 * PZ0 * cz + cz * cz - R * R
    # Дескриминант
    D = B * B - 4 * A * C
    if D < 0:
        return print("Коллизий не найдено")
    t1 = (-B - math.sqrt(D)) / (2.0 * A)
    sol1 = [PX0 * (1 - t1) + t1 * PX1, PY0 * (1 - t1) + t1 * PY1, PZ0 * (1 - t1) + t1 * PZ1]
    t2 = (-B + math.sqrt(D)) / (2.0 * A)
    sol2 = [PX0 * (1 - t2) + t2 * PX1, PY0 * (1 - t2) + t2 * PY1, PZ0 * (1 - t2) + t2 * PZ1]

    if (t1 > 1 or t1 < 0) and (t2 > 1 or t2 < 0):
        return print("Коллизий не найдено")
    elif (t1 < 1 or t1 > 0) and (t2 > 1 or t2 < 0):
        return print("Точка с Х: {} , Y: {} , Z: {}".format(*sol1))
    elif (t1 > 1 or t1 < 0) and (t2 < 1 or t2 > 0):
        return print("Точка с Х: {} , Y: {} , Z: {}".format(*sol2))
    elif D == 0:
        return print("Точка с Х: {} , Y: {} , Z: {}".format(*sol1))
    else:
        return print("Точка с Х: {} , Y: {} , Z: {} \nа также Точка с Х: {} , Y: {} , Z: {}".format(*sol1, *sol2))


if __name__ == '__main__':
    handle = open(r"test.txt", 'r')
    stroke = handle.readline()
    while stroke:
        cent = re.findall(r'center: \[(\S+), (\S+), (\S+)\][,|}]', stroke)
        R = re.findall(r'radius: (\S+[^}])[}|,]', stroke)
        line0 = re.findall(r'line: \{\[(\S+), (\S+), (\S+)\],', stroke)
        line1 = re.findall(r'\],\s\[(\S+), (\S+), (\S+)\]\}', stroke)
        radius = float(R[0])
        centrx = float(cent[0][0])
        centry = float(cent[0][1])
        centrz = float(cent[0][2])
        PointX0 = float(line0[0][0])
        PointY0 = float(line0[0][1])
        PointZ0 = float(line0[0][2])
        PointX1 = float(line1[0][0])
        PointY1 = float(line1[0][1])
        PointZ1 = float(line1[0][2])
        checkPoint(centrx, centry, centrz, radius, PointX0, PointY0, PointZ0, PointX1, PointY1, PointZ1)
        print('\n')
        stroke = handle.readline()
    handle.close()
