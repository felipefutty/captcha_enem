# Quebrando captcha ENEM
Resolução do CAPTCHA usado pelo ENEM, usando CNN.

Usa-se duas abordagens diferentes, com mesmo CNN e parâmetros de treinamento, mudando apenas a forma de enxergar a base criada:

1. **Base Integral:** usar a base de dados criadas de forma integrau, removendo apenas captchas com 9 caracteres (muito raro e aumentaria o problema). Logo, essa rede resolve captchas sem saber o tamanho indo de 3 até 9. **Acuracia:** 3 captchas de 500 (3/500=0,6% de acerto)

2. **Base Parcial**: Cria uma base com os captchas de 5 caracteres, somente. Cortando a imagem desses captcha em 5 pedaçoes iguais, ou seja, criando uma base com apenas 1 caracter por imagem. Dessa forma, a rede treinada consegue dizer qual caracter é baseado em uma imagem 37x50 pixels contendo um caracter. **Acuracia:**  63 captchas de 99 (63/99=63,63% de acerto) 


**IMPORTANTE ANTES DE EXECUTAR DESCOMPACTE AS BASES DE DADOS***
# Executando Base de Teste

Ambas abordagens já possuem a rede treinada com 100 epochs e com configurações exatamente iguais, mudando apenas a base de dados usadas. Para executar usa-se:

1. **Base Integral:** 
	```
	python entire_captcha_code/captcha_load_test.py
	```
2. **Base Parcial:** 
	```
	python five_captcha_code/captcha_load_test.py
	```

# Executando treinamento
Para rodar cada um dos testes com as bases diferentes (ira sobreescrever o modelo/pesos da rede treinada que esta nesse projeto):

1. **Base Integral:** 
	```
	python five_captcha_code/captcha_load_test.py
	```
2. **Base Parcial:** 
	```
	python entire_captcha_code/captcha_load_test.py
	```

# Referencia

Foi modificado a implementacao do [ github scnuhealthy](https://github.com/scnuhealthy/cnn_keras_captcha)
