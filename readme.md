# OCR PDF to TXT

`Ocr_Pdf_To_Txt.py` é um script em Python que realiza o reconhecimento óptico de caracteres (OCR) em arquivos PDF, extraindo o texto de suas páginas e salvando-o em um arquivo de texto (TXT).

## Recursos
- Conversão de PDFs para imagens usando a biblioteca `wand`.
- Processamento de imagens com OCR utilizando `pyocr` e `Pillow`.
- Suporte para idiomas configuráveis no OCR.
- Detecção de orientação opcional.
- Exportação de texto consolidado em um arquivo TXT.

## Requisitos

Certifique-se de que você tem os seguintes requisitos instalados no seu ambiente:

### Dependências do Sistema
- Python 3.8 ou superior
- ImageMagick (para suporte à biblioteca `wand`)

### Dependências do Python

Instale as dependências listadas abaixo com o comando:

```bash
pip install wand pillow pyocr
```

## Uso

### Execução Básica

Execute o script com os seguintes argumentos:

```bash
python Ocr_Pdf_To_Txt.py <input_pdf> <output_txt> [<resolution>] [<ocr_language>] [<image_format>] [<orientation_test>]
```

### Argumentos

| Argumento             | Descrição                                                                                  | Padrão       |
|-----------------------|----------------------------------------------------------------------------------------------|--------------|
| `input_pdf`           | Caminho do arquivo PDF de entrada.                                                         | Obrigatório  |
| `output_txt`          | Caminho do arquivo TXT onde o texto extraído será salvo.                                    | Obrigatório  |
| `resolution`          | Resolução do PDF em DPI para conversão de imagens.                                         | `300`        |
| `ocr_language`        | Idioma utilizado para o OCR. Deve ser um dos suportados pela ferramenta OCR instalada.     | `eng`        |
| `image_format`        | Formato das imagens geradas a partir do PDF (por exemplo, `png`).                          | `png`        |
| `orientation_test`    | Realiza teste de orientação para corrigir textos rotacionados (`True` ou `False`).         | `True`       |

### Exemplo de Execução

```bash
python Ocr_Pdf_To_Txt.py sample.pdf output.txt 300 eng png True
```

## Saída
- O texto extraído de cada página do PDF será salvo no arquivo TXT especificado.
- Informações sobre o progresso do OCR e tempo de execução serão exibidas no console.

## Estrutura do Código

- **Classe `LocalOCR`**: Contém métodos para configurar o OCR, processar PDFs e extrair texto de imagens.
- **Função Principal**: Recebe os argumentos CLI, instancia a classe `LocalOCR`, processa o PDF e salva o texto extraído no arquivo de saída.

## Considerações
- Certifique-se de que o `ImageMagick` está instalado e configurado corretamente no seu sistema.
- Verifique se o idioma escolhido para OCR está disponível na sua instalação do Tesseract OCR.

## Problemas Conhecidos
- PDFs protegidos por senha não podem ser processados diretamente.
- Desempenho pode ser afetado por PDFs muito grandes ou de alta complexidade.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

