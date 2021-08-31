
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:  #utf-8-sig解決中文編碼開頭的怪怪字(\ufeff)
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Bobo':
            person = 'Bobo'
            continue
        elif line == 'Jinjin':
            person = 'Jinjin'
            continue
        if person: #如果person有值
            new.append(person + ':' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)
main()

