from sklearn.linear_model import Perceptron
from pprint import pprint

cor_vermelho = 0
cor_amarelo = 1

apples = [[10, cor_vermelho], [2, cor_vermelho]]
bananas = [[20, cor_amarelo], [10, cor_amarelo]]

X = []
X.extend(apples)
X.extend(bananas)

apple_tag = 5
banana_tag = 10

y = [apple_tag, apple_tag, banana_tag, banana_tag]

perceptron = Perceptron(max_iter=5000)

perceptron.fit(X, y)

what_fruit = [[6, cor_vermelho], [15, cor_amarelo]]

pprint(perceptron.predict(what_fruit))

arg = {5: 'maçã', 10: 'banana'}

classes = [arg[c] for c in perceptron.classes_]

pprint(classes)

cm, color = int(input("digite cm: ")), int(input("digite cor: "))

test_input = [[cm, color]]

tag_pred = perceptron.predict(test_input)
classe = [arg[c] for c in tag_pred]

print(tag_pred)
pprint(classe)



what_fruit = [[6, cor_vermelho], [15, cor_amarelo]]
