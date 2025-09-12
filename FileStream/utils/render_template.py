import aiohttp
import jinja2
import urllib.parse
from FileStream.config import Telegram, Server
from FileStream.utils.database import Database
from FileStream.utils.human_readable import humanbytes

db = Database(Telegram.DATABASE_URL, Telegram.SESSION_NAME)

async def render_page(db_id):
    try:
        file_data = await db.get_file(db_id)
        if not file_data:
            return "Fichier non trouvé"
        
        src = urllib.parse.urljoin(Server.URL, f'dl/{file_data["_id"]}')
        file_size = humanbytes(file_data['file_size'])
        file_name = file_data['file_name'].replace("_", " ")
        mime_type = file_data.get('mime_type', 'video/mp4')
        
        if mime_type.startswith('video/') or mime_type.startswith('audio/'):
            template_file = "FileStream/template/play.html"
        else:
            template_file = "FileStream/template/dl.html"
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.head(src) as response:
                        if 'Content-Length' in response.headers:
                            file_size = humanbytes(int(response.headers['Content-Length']))
            except:
                pass

        with open(template_file, 'r', encoding='utf-8') as f:
            template = jinja2.Template(f.read())

        return template.render(
            file_name=file_name,
            file_url=src,
            file_size=file_size,
            mime_type=mime_type
        )
        
    except Exception as e:
        logging.error(f"Error rendering page: {e}")
        return f"Erreur: {str(e)}"