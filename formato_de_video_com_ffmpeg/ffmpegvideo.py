
# https://ffmpeg.org/download.html#build-windows
# https://github.com/BtbN/FFmpeg-Builds/releases

"""
Codificaçlão usada

ffmpeg -i "Entrada" -i "Legenda_se_tiver" -c:v libx264 -crf 23 -preset ultrafast -c:a aac
-b:a 320k -c:s srt -map v:0 -map a _map 1:0 -ss 00:00:00 -to 00:00:10 "Saida"

"""
from caminho import caminho_base
import os
import sys
import fnmatch


if sys.platform == 'linux':
    comand_ffmpeg = 'ffmpeg'
else:
    # Esse cominho é referente os CODEXs usados para conversão,
    # Se A pasta não existir, Deve ser criada e colocado o caminho correto abaixo.
    # O arquivo "ffmpeg-master-latest-win64-gpl"
    # foi tirado do gitHub(https://github.com/BtbN/FFmpeg-Builds/releases)
    comand_ffmpeg = (f'{caminho_base}')


codec_video = '-c:v libx264'
codec_audio = '-c:a aac'
crf = '-crf 23'
preset = '-preset fast'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'


def convertvideo(path, ext):
    root, file = os.path.split(path)
    extenssao = ext

    if not fnmatch.fnmatch(file, '*.mp4'):
        pass

    caminho = os.path.join(root, file)
    name_file, ext_file = os.path.splitext(caminho)
    caminho_legenda = name_file + '.srt'

    if os.path.isfile(caminho_legenda):
        input_legenda = f'-i "{caminho_legenda}"'
        map_legenda = '-c:s srt -map v:0 a -map a -map 1:0'
    else:
        input_legenda = ''
        map_legenda = ''

    nome_file_t, ext = os.path.splitext(file)
    novo = f'{nome_file_t}_New{extenssao}'
    file_exite = os.path.join(root, novo)

    comando = f'{comand_ffmpeg} -i "{caminho}" {input_legenda} {codec_video} ' \
                f'{crf} {preset} {codec_audio} {bitrate_audio} {map_legenda} {file_exite}'
    
    os.system(comando)
    
    return 'ok'
