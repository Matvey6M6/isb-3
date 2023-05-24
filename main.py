import argparse
import json
import logging
import os

from  keys_generator import keys_generator
import  encryption 
import decryption
logging.basicConfig(level=logging.INFO)

def check_size(size):
    if(size != 128 or size != 192 or size !=256):
         return 128 , False
    return size , True

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    mode_group = parser.add_mutually_exclusive_group(required=True)

    mode_group.add_argument(
        '-gen', '--generation', action='store_true', help='Запуск генерации ключей')
    mode_group.add_argument('-enc', '--encryption', action='store_true',
                            help='Запуск шифрования')
    mode_group.add_argument('-dec', '--decryption', action='store_true',
                            help='Запуск расшифрования')
    parser.add_argument('config_file', metavar='N',
                        type=str, help='Установить свой конфиг файл')
    args = parser.parse_args()
    mode = (args.generation, args.encryption, args.decryption)
    SETTINGS = os.path.join(args.config_file)
    settings = str()
    try:
        with open(SETTINGS) as json_file:
            settings = json.load(json_file)
    except:
        logging.error(f"Не найден json файл")
        exit()
    size = int(settings["size"])
    size, flag = check_size(size)
    if not flag :
        logging.info('Размер ключа не тот. Выбран дефолтный размер: 128.')
    else:
        logging.info(f'Размер принят: {size}' )

    if (mode == (True, False, False)):
            try:
                keys_generator(
                settings['private_key'], settings['public_key'], settings['symmetric_key'], settings['symmetric_key_decrypted'], size)
                logging.info('Ключи успешно сгенерированны')
            except:
                 logging("НЕ получилось сгенерировать ключи ")
    elif( mode == (False, True, False)):
            try:
                encryption.encrypt_data(settings['src_text_file'], settings['private_key'],
                         settings['symmetric_key'], settings['encrypted_file'], settings["symmetric_key_decrypted"], size)
                logging.info('Данные зашифрованный')
            except:
                 logging.info("Отмена шифрования данных")
    elif(mode ==  (False, False, True)):
            try:           
                decryption.decrypt_data(settings['encrypted_file'], settings['private_key'],
                         settings['symmetric_key'], settings['decrypted_file'], settings["symmetric_key_decrypted"], size)
                logging.info('Данные успешно расшифрованны')
            except:
                 logging.info("Ошибка при дешифрации см выше")
    else:
            logging.error("Режим прогроммы не выбран")