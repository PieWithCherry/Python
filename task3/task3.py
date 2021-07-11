import re
from collections import Counter
import csv
from sys import argv

filename = argv[1]


def reader_up(filename):
    with open(filename, encoding='utf-8') as f:
        log = f.read()
        up = re.findall(r'up\s\d+l\s\((успех)\)', log)
        f.close()
    return up


def readar_in_v(filename):
    with open(filename, encoding='utf-8') as f:
        log = f.read()
        gen = re.findall(r'(\d+)\s\(объем бочки\)', log)
        v = int(gen[0])
        sub = re.findall(r'(\d+)\s\(текущий объем воды в бочке\)', log)
        cur = int(sub[0])
        value = cur
        done = re.findall(r'up\s(\d+)l\s\(успех\)', log)
        scdo = re.findall(r'scoop\s(\d+)l\s\(успех\)', log)
        for i in done:
            value += int(i)
        for j in scdo:
            value -= int(j)
        f.close()
        return value


def reader_start_v(filename):
    with open(filename, encoding='utf-8') as f:
        log = f.read()
        sub = re.findall(r'(\d+)\s\(текущий объем воды в бочке\)', log)
        cur = int(sub[0])
        f.close()
        return cur


def reader_data(filename):
    with open(filename, encoding='utf-8') as f:
        log = f.read()
        data = re.findall(r'(\d{,4}\-\d{,2}\-\d{,2}\w\d{,2}\:\d{,2}\:\d{,2})\.', log)
        f.close()
    return data


def reader_fail(filename):
    with open(filename, encoding='utf-8') as f:
        log = f.read()
        sc = re.findall(r'\s\d+l\s(\(фейл\))', log)
        f.close()
    return sc


def reader_succes(filename):
    with open(filename, encoding='utf-8') as f:
        log = f.read()
        scs = re.findall(r'\s\d+l\s(\(успех\))', log)
        f.close()
    return scs


def reader_scoop_done(filename):
    with open(filename, encoding='utf-8') as f:
        log = f.read()
        scdo = re.findall(r'scoop\s(\d+)l\s\(успех\)', log)
        f.close()
    return scdo


def reader_scoop_fail(filename):
    with open(filename, encoding='utf-8') as f:
        log = f.read()
        scno = re.findall(r'scoop\s(\d+)l\s\(фейл\)', log)
        f.close()
    return scno


def reader_done_up(filename):
    with open(filename, encoding='utf-8') as f:
        log = f.read()
        done = re.findall(r'up\s(\d+)l\s\(успех\)', log)
        f.close()
    return done


def reader_done_fail(filename):
    with open(filename, encoding='utf-8') as f:
        log = f.read()
        done = re.findall(r'up\s(\d+)l\s\(фейл\)', log)
        f.close()
    return done


def summ(done):
    summa = 0
    for i in done:
        summa += int(i)
    return summa


def counter(up):
    count = Counter(up)
    return count


def write_csv_try(count):
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['Попыток налить воду в бочку:', 'Значение']
        writer.writerow(header)
        for item in count:
            writer.writerow((item, count[item]))


def write_csv_fail(out):
    with open('output.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['Процент неудачных попыток', f'{out} %']
        writer.writerow(header)


def write_csv_sum(done, pref):
    with open('output.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = [f'Количество воды, которую {pref} налили', done]
        writer.writerow(header)


def write_csv_out(done, pref):
    with open('output.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = [f'Количество воды, которую {pref} забрали', done]
        writer.writerow(header)


def write_csv_start(count):
    with open('output.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['Изначальное кол-во воды в бочке: ', count]
        writer.writerow(header)


def write_csv_value(count):
    with open('output.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['После всех операций воды осталось: ', count]
        writer.writerow(header)


def failProc(sc, up):
    out = len(sc) * 100 / (len(sc) + len(up))
    return out


if __name__ == "__main__":
    write_csv_try(counter(reader_up(filename)))
    write_csv_fail(failProc(reader_fail(filename), reader_succes(filename)))
    write_csv_sum(summ(reader_done_up(filename)), '')
    write_csv_sum(summ(reader_done_fail(filename)), 'не')
    write_csv_out(summ(reader_scoop_done(filename)), '')
    write_csv_out(summ(reader_scoop_fail(filename)), 'не')
    write_csv_start(reader_start_v(filename))
    write_csv_value(readar_in_v(filename))
    print('csv файл был успешно создан!')
