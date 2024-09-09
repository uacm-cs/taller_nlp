import unicodedata
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import word_tokenize
from sklearn.svm import LinearSVC


PUNCTUACTION = ";:,.\\-\"'/"
SYMBOLS = "()[]¿?¡!{}~<>|"
NUMBERS = "0123456789"
SKIP_SYMBOLS = set(PUNCTUACTION + SYMBOLS)
SKIP_SYMBOLS_AND_SPACES = set(PUNCTUACTION + SYMBOLS + '\t\n\r ')


class ClasificadorTODO:
    
    def __init__(self):
        # TODO: Obtener STOPWORDS, descargar stopwords en caso de que no estén disponibles

        # TODO: Definir el  clasificador  LinearSVC        
        self.clasificador_svc = LinearSVC(random_state=42)

        # TODO: Definir los parámetros para el modelo de vectorización  TFVectorizer o  TfidfVectorizer con el uso de unigramas 

    def normaliza_texto(self, input_str,
                        punct=False,
                        accents=False,
                        num=False,
                        max_dup=2):
        """
        TODO: Explicar en más detalle cada parámetro de la función

        Esta función normaliza el texto eliminando puntuación, números, acentos y duplicados de caracteres
        punct=False (elimina la puntuación, True deja intacta la puntuación)
        accents=False (elimina los acentos, True deja intactos los acentos)
        num=False (elimina los números, True deja intactos los números)
        max_dup=2 (número máximo de símbolos duplicados de forma consecutiva, rrrrr => rr)
        """
        nfkd_f = unicodedata.normalize('NFKD', input_str)
        n_str = []
        c_prev = ''
        cc_prev = 0
        for c in nfkd_f:
            if not num:
                if c in NUMBERS:
                    continue
            if not punct:
                if c in SKIP_SYMBOLS:
                    continue
            if not accents and unicodedata.combining(c):
                continue
            if c_prev == c:
                cc_prev += 1
                if cc_prev >= max_dup:
                    continue
            else:
                cc_prev = 0
            n_str.append(c)
            c_prev = c
        texto = unicodedata.normalize('NFKC', "".join(n_str))
        texto = re.sub(r'(\s)+', r' ', texto.strip(), flags=re.IGNORECASE)
        return texto

    # Preprocesamiento personalizado 
    def mi_preprocesamiento(self, texto):
        # TODO: Normalización de texto
        #  - Convertir  a minúsculas el texto antes de normalizar
        #  - Separar oraciones
        #  - Separar tokens
        #  - Normalizar texto

        return None

    # Tokenizador personalizado 
    def mi_tokenizador(self, texto):
        # TODO: Explorar otros métodos de eliminación de stopwords o reducción de características como stemming o lematización
        # - Eliminar stopwords

        return None

    def vectorizar(self, texto):
        print("Vectorizando texto")
        # TODO: Vectorizar el texto proporcionado en el mismo espacio de representación aprendido de los datos de entrenamiento
        # - Retorna el texto vectorizado de acuerdo a la misma representación del modelo de texto creado en la etapa fit
        return None

    def fit(self, X_train, Y_train):
        print("Inicio de entrenamiento")
        print("Construyendo del modelo de representación del texto con los datos de entrenamiento")
        # TODO: Construir el modelo de representación del texto con el pesado correspondiente con el conjunto de datos X_train

        # TODO: Construir el modelo de representación del texto con el pesado correspondiente con el conjunto de datos X_train

        # TODO: Entrenar el modelo del clasificador con los datos de entrenamiento transformados en la matriz Documento-Término y con las clases conocidas
        
        print("Fin de entrenamiento")


    def setLabelEncoder(self, label_encoder):
        self.label_encoder = label_encoder
    


    def predict(self, texto):
        print("Prediciendo nuevos datos")
        # Predecir la clase de acuerdo con el modelo de clasificador creado
        
        # TODO: Convertir los datos de entrada "texto" dentro del espacio de representación del modelo de texto de entrenamiento (Vectorizar)

        # TODO: Predir los datos con el modelo del clasificador entrenado 
        
        # TODO: Convertir las etiquetas del clasificador a su versión original del LabelEncoder

        return None