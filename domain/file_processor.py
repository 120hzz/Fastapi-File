import os
import csv

from fastapi import HTTPException, status

class FileProcessor:
    """Manager of files and folder processor."""

    def __init__(self):
        self.file_path = 'data/seu_file.csv'
        self.directory = 'data'

    def create_file(self):
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['conta', 'agencia', 'texto', 'valor'])
                return {"mensagem" : f"Arquivo {self.file_path} criado com sucesso."}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Arquivo já existe.")

    async def upload_file(self, file: UploadFile):
        """
        Upload a file to read and print data
        :param file: uploaded file
        :return success or error
        """
        if file.filename.endswith('.csv'):
            try:
                csv_reader = csv_DictReader(file.file)
                for row in csv_reader:
                    data = {'conta': row[0],
                            'agencia': row[1],
                            'texto': row[2]
                            'valor': float(row[3])
                            }
                    print(data)
            except Exception as e:
                raise HTTPException(status_code:status.HTTP_400_BAD_REQUEST,
                detail=f"Falha ao processar o arquivo CSV: {str(e)}")
        else:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail="Arquivo não possui o formato suportado.")