def process_hex_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Разделяем строку на смещение, данные и текст
            offset = line[:8]
            hex_part = line[9:58].replace(" ", "")  # Убираем пробелы из шестнадцатеричных данных
            text_part = line[62:].replace(" ", "").strip()  # Убираем пробелы из текстовой части

            # Разделяем шестнадцатеричные данные на группы по 4 символа с добавлением пробелов
            formatted_hex = ' '.join([hex_part[i:i+4] for i in range(0, len(hex_part), 4)])

            # Выравниваем отступы, добавляя пробелы между колонками и добавляя ":" после offset
            formatted_line = f"{offset}: {formatted_hex:<39}  {text_part}"  # 2 пробела перед текстом

            # Записываем строку в файл
            outfile.write(formatted_line + '\n')

# Пример использования
input_file = 'wireshark_jpg.hex'
output_file = 'fixed.hex'
process_hex_file(input_file, output_file)
