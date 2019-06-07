#resources: https://www.youtube.com/watch?v=fS70iptz-XU&list=PL6SXJNGTndC7gBrOoLGo45McH5tvUf8df&index=2&t=2571s
# https://graphviz.gitlab.io/_pages/Download/Download_windows.html
# todo: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html
import pandas
from  sklearn import tree, model_selection
import utils

#33:20
train = pandas.read_csv("C:\\Users\\jurgend\\Apps\\reverse-decision-tree-punching\\OpenRulesOutput2.csv",sep=";", decimal=",")
utils.clean_data(train)
#print(train.shape)
#print(train.count())

target = train["Machine1"].values
#1! features_names = ["Shape", "DifficultArtwork","LongFace", "ShortFace", "Bars","Transparant"] 
#ook 1:
features_names = ["Shape", "DifficultArtwork","LongFace", "Transparant"]
#features_names = ["Shape"]
#shape: 72%; +LongFace: 83; + ShortFace:83%; Bars:
features = train[features_names].values

#decision_tree = tree.DecisionTreeClassifier(criterion='gini', random_state=1)
decision_tree = tree.DecisionTreeClassifier(criterion='entropy', random_state=1)

decision_tree_ = decision_tree.fit(features,target)
print(decision_tree_.score(features, target))

tree.export_graphviz(decision_tree_, feature_names=features_names,out_file="C:\\Users\\jurgend\\Apps\\reverse-decision-tree-punching\\reverse-decision-tree-entropy.dot")



