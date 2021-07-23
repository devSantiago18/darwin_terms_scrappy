import os
import platform
import asyncio

separador = "\\" if platform.system() == "Windows" else "/"
modules_to_excecute = ['main.py', 'quick_reference_scrappy.py', 'comparing.py', "excel_forma.py"]


async def create_folders():
    os.system(f'mkdir  resources{separador}json')
    os.system(f'mkdir resources{separador}pages')
    os.system('mkdir build')


async def exc_module(module):
    os.system(f'python {module}')


async def main():
    folder_task = asyncio.create_task(create_folders())
    await folder_task
    
    for x in modules_to_excecute:
        aux_corrutine_task = asyncio.create_task(exc_module(x))
        await aux_corrutine_task


asyncio.run(main())
    