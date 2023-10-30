from telethon import TelegramClient, events, types
import time
from os.path import exists
import subprocess
import os
import sys
from telethon.tl.types import DocumentAttributeFilename

api_hash="131b576240be107210aace99a5f5c5b0"
api_id="9024532"
bot_token="6431169915:AAECb_NSpWWVbG1Qz7r4itK1f75yQxrIjAY"

client = TelegramClient('BashEBOT', api_id, api_hash).start(bot_token=bot_token)

envs = {}

def ejecutar_comando(command, env_id):
    if env_id in envs:
        # Cambiar el directorio de trabajo al directorio del ambiente
        os.chdir(envs[env_id])
    else:
        # Crear el directorio del ambiente
        env_dir = f"ambiente_{env_id}"
        if not exists(env_dir):
        	os.makedirs(env_dir)
        envs[env_id] = env_dir
        # Cambiar el directorio de trabajo al directorio del ambiente
        os.chdir(env_dir)
        
    # Ejecutar el comando
    try:
    	resultado = subprocess.getoutput(command)
    except:
    	None

    # Volver al directorio de trabajo original
    os.chdir("..")
    if resultado == '':
    	resultado = "Hecho!"
    # Tratar los diferentes tipos de resultados
    if isinstance(resultado, str):
        return resultado
    elif isinstance(resultado, list):
        return "\n".join(resultado)
    elif isinstance(resultado, bytes):
        return resultado.decode("utf-8", "ignore")
    else:
        return str(resultado) 

def destruir_ambiente(env_id):
    # Verificar si el ambiente existe
    if env_id in envs:
        # Eliminar el directorio del ambiente y eliminarlo del diccionario
        os.rmdir(envs[env_id])
        del envs[env_id]
        
@client.on(events.NewMessage)
async def my_event_handler(event):
    user = event.sender
    if not exists("users"):
        	open("users","w").write("5692000351 2055672924")
    if str(user.id) in open("users","r").read():
    	if "/start" in event.raw_text:
    		await client.send_message(user.id,'<b>BIENVENIDO A BASHE</b>\n\n<i>BashE es un potente ejecutor de comandos bash preparado para tus proyectos.</i>\n\n <b>🏁Puedes comenzar a crear:</b>\n\n<code>$ echo "Hola mundo"</code>\n\n <b>🎦CONVERTIDOR DE VIDEOS</b>\n\n<code>$ ffmpeg -i [VIDEO] -vf "scale=480:240" -c:v libx264 -crf 20 -preset veryfast -c:a copy [NUEVO VIDEO]</code>\n\n <b>🔍LECTOR DE IMAGENES OCR</b>\n\n<code>$ tesseract [IMAGEN] stdout</code>\n\n <b>📚ZIPS SPLIT</b>\n\n<code>$ 7z a -v[TAMAÑO]m [NOMBRE COMPRIMIDO].7z [NOMBRE DEL ARCHIVO A COMPRIMIR]</code>\n\n <b>🚀PYTHON DEPLOY</b>\n\n<code>$ python3 [ARCHIVO PYTHON]</code>\n\n <b>🔗DESCARGADOR POR URL</b>\n\n<code>$ curl -O [URL]</code>\n\n <b>⏬DESCARGADOR DE DOCUMENTOS Y VIDEOS DE TELEGRAM</b>\n\n<code>SUBE O REENVÍA TU ARCHIVO</code>\n\n <b>⏫CARGADOR DE ARCHIVOS A TELEGRAM</b>\n\n<code>/upload [ARCHIVO]</code>\n\n<b>¡¡BASH ES TU LÍMITE!!</b>\n\n\n<b>CREADO POR:</b><i>@l_tech_dev_l</i>', parse_mode='HTML')
    	elif '/upload' in event.raw_text:
    		msg = await client.send_message(user.id,"<b>^^SUBIENDO A TELEGRAM^^</b>", parse_mode='HTML')
    		await client.send_file(user.id ,file="./ambiente_"+str(user.id)+'/'+event.raw_text.split(" ")[1])
    		await client.delete_messages(user.id, msg.id)
    	elif event.media:
    		if event.file:
    			file_path = './ambiente_'+str(user.id)+"/";
    			filename = 'sin_nombre.bashe';
    			try:
    				attributes = event.media.document.attributes
    				for attr in attributes:
    			         if isinstance(attr, types.DocumentAttributeFilename):
    			         	filename = attr.file_name
    			         	file_path = os.path.join(file_path, attr.file_name)
    				msg = await client.send_message(user.id,'<b>-~DESCARGANDO~-</b>\n\n<i>VER ESTADO </i><code> $ stat -c %s '+filename+'</code>', parse_mode='HTML')
    				download = await client.download_media(event.media, file=file_path)
    				await client.edit_message(user.id, msg.id, "<b>°•°DESCARGADO°•°</b>\n\n <i>REVISAR </i><code>$ ls</code>", parse_mode='HTML')
    			except:
    				await client.send_message(user.id,'<b>NO SE ADMITEN FOTO, POR FAVOR ENVÍE LA IMÁGEN COMO DOCUMENTO</b>', parse_mode='HTML')
    	elif '/destruir' in event.raw_text:
    		destruir_ambiente(user.id)
    		await client.send_message(user.id,"<b>×AMBIENTE DESTRUIDO×</b>", parse_mode='HTML')
    	elif "/addUser_@A1a2a3mo" in event.raw_text:
    		open("users","w").write(open("users", "r").read()+" "+str(event.raw_text.split(" ")[1]))
    		await client.send_message(user.id, "USUARIO AÑADIDO")
    	elif "$" in event.raw_text:
    		if "../" in event.raw_text:
    			await client.send_message(user.id,"<b>×COMANDO ILEGAL SI CONTINUA SERÁ BANEADO SIN DERECHO DE RECLAMO×</b>", parse_mode='HTML')
    		else:
    			mes = await client.send_message(user.id,"<b>SU CÓDIGO ESTA CORRIENDO...</b>", parse_mode='HTML')
    			result = ejecutar_comando(event.raw_text.split("$ ")[1], user.id)
    			await client.edit_message(user.id, mes.id,"<code>"+result+"</code>", parse_mode='HTML')
    	else:
    		await client.send_message(user.id,'<b>×COMANDO DESCONOCIDO×</b>', parse_mode='HTML')
    else:
        await client.send_message(user.id,'<b>BIENVENIDO A BASHE</b>\n\n<i>BashE es un potente ejecutor de comandos bash preparado para tus proyectos.</i>\n\n <b>🏁Puedes comenzar a crear:</b>\n\n<code>$ echo "Hola mundo"</code>\n\n <b>🎦CONVERTIDOR DE VIDEOS</b>\n\n<code>$ ffmpeg -i [VIDEO] -vf "scale=480:240" -c:v libx264 -crf 20 -preset veryfast -c:a copy [NUEVO VIDEO]</code>\n\n <b>🔍LECTOR DE IMAGENES OCR</b>\n\n<code>$ tesseract [IMAGEN] stdout</code>\n\n <b>📚ZIPS SPLIT</b>\n\n<code>$ 7z a -v[TAMAÑO]m [NOMBRE COMPRIMIDO].7z [NOMBRE DEL ARCHIVO A COMPRIMIR]</code>\n\n <b>🚀PYTHON DEPLOY</b>\n\n<code>$ python3 [ARCHIVO PYTHON]</code>\n\n <b>🔗DESCARGADOR POR URL</b>\n\n<code>$ curl -O [URL]</code>\n\n <b>⏬DESCARGADOR DE DOCUMENTOS Y VIDEOS DE TELEGRAM</b>\n\n<code>SUBE O REENVÍA TU ARCHIVO</code>\n\n <b>⏫CARGADOR DE ARCHIVOS A TELEGRAM</b>\n\n<code>/upload [ARCHIVO]</code>\n\n\n<b>¡¡BASH ES TU LÍMITE!!</b>\n\n\n<b>CREADO POR:</b><i>@l_tech_dev_l</i>\n\n\n\n××LAMENTABLEMEMTE NO TIENES ACCESO A ESTE BOT××', parse_mode='HTML')
        

@client.on(events.InlineQuery)
async def handle_inline_query(event):
        user = event.sender
        query = event.text  # Obtén la consulta del usuario
        if "../" in query:
        	result = "×COMANDO ILEGAL SI CONTINUA SERÁ BANEADO SIN DERECHO DE RECLAMO×"
        else:
        	result = query+"\n\n"+ejecutar_comando(query, user.id)
        # Crear una lista de resultados
        if str(user.id) in open("users","r").read():
            results = [
            await event.builder.article(
                title='Resultado',
                description="Presione para enviar el resultado de su código.",
                text=result
            )
        ]
        else:
        	results = [await event.builder.article(title='ERROR', description="Usted no es un usuario del bot.", text="Estoy intentando usar un bot de TechDev, pero no estoy permitido, F :(")]

        await event.answer(results)


print("BOT INICIADO")
client.run_until_disconnected()
