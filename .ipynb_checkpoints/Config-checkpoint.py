#Variables categoricas con NA
CATEGORICAL_VARS_WITH_NA_FREQUENT = []

#Variable categoricas con NA pero indicador de Missing
CATEGORICAL_VARS_WITH_NA_MISSING = []

#Variables para hacer mapeo categorico por codificación ordinal
NivelEducativo_VARS = ['NivelEducativo']

EstadoCivil_VARS = ['EstadoCivil']

#Variables numéricas con NA
NUMERICAL_VARS_WITH_NA = ['Ingreso']

DROP_FEATURES = ['MIS', 'InicioCliente','Cumpleaños']

NUMERICALS_LOG_VARS = ['ComprasTienda','VisitasWeb','Ingreso']

NUMERICALS_YEJ_VARS = ['AlimentosFrescos','Vinos','Carnes','Oro','ComprasTienda','TotalProductos','Edad']

#Variables para binarización por sesgo fuerte
BINARIZE_VARS = ['AceptaCompra1','AceptaCompra2','AceptaCompra3','AceptaCompra4','AceptaCompra5','Quejas','TieneNiños','TieneAdolecentes']

#Variables categoricas a codificar sin ordinalidad
CATEGORICAL_VARS = ['NivelEducativo' ]

TOTAL_PRODUCTOS = ['AlimentosFrescos','Vinos','Frutas','Carnes','Dulces','Oro']
VACIO_MAPPINGS = ['']
#Mapeos de variables categoricas
NivelEducativo_MAPPINGS = {'Graduation':1, 'PhD':2, 'Master':3, 'Basic':4, '2n Cycle':5, 'Missing':0, 'NA':0, 'NaN':0}

EstadoCivil_MAPPINGS = {'Married':1, 'Single':2, 'Together':3, 'Divorced':4, 'Widow':5, 'Absurd':6, 'Alone':7, 'YOLO':8, 'Missing':0, 'NA':0, 'NaN':0}

#Variables seleccionadas según análisis de Lasso
FEATURES = [
    'Ingreso','EstadoCivil', 'AlimentosFrescos', 'Frutas', 'Carnes', 'Pescado', 'Oro',
       'ComprasCatalogo', 'ComprasTienda', 'VisitasWeb', 'AceptaCompra1',
       'AceptaCompra2', 'AceptaCompra3', 'AceptaCompra4', 'AceptaCompra5',
       'TotalCompras', 'Antiguedad', 'TieneNiños', 'TieneAdolecentes','Quejas','NivelEducativo','Vinos','TotalProductos','Edad',
]