import aiohttp
import asyncio
import json

class ItemMaterial:
  def __init__(self, code):
    self.code = code

  async def fetch_material_data(codigo_item_material: str) -> dict:
    url = f"https://cnbs.estaleiro.serpro.gov.br/cnbs-api/material/v1/recuperaDadosItemMaterialPorCodigo?codigo_item_material={codigo_item_material}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            raise Exception(f"Error fetching material data: {response.status}")

  async def fetch_unidade_fornecimento(codigo_pdm: str) -> dict:
    url = f"https://cnbs.estaleiro.serpro.gov.br/cnbs-api/material/v1/unidadeFornecimentoPorCodigoPdm?codigo_pdm={codigo_pdm}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            raise Exception(f"Error fetching unidade fornecimento: {response.status}")

async def main():
    try:
        # Gerar resposta do material
        material_data = await ItemMaterial.fetch_material_data("336956")
        # Gerar resposta da unidade de medida
        pdm_code = material_data["codigoPdm"]
        
        if not pdm_code:
            raise Exception("PDM code not found")
          
        # Gerar resposta da unidade de medida
        unidade_data = await ItemMaterial.fetch_unidade_fornecimento(pdm_code)
        
        # Print results
        print("Material Data:", json.dumps(material_data, indent=2))
        print("Unidade Fornecimento:", json.dumps(unidade_data, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())