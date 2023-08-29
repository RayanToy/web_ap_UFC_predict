from django.shortcuts import render
from django.views.generic import TemplateView
from .models import features
from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from .forms import FeaturesForm

ufc_data = pd.read_csv(r"D:\Загрузки\Ufc_Dt (1).csv")
ufc_data.drop("Unnamed: 0", axis=1, inplace=True)
label = ufc_data.Winner
ufc_data = ufc_data.drop('Winner', axis=1)
X_train, X_valid, y_train, y_valid = train_test_split(ufc_data, label, random_state=0, test_size=0.3)


class HomeView(TemplateView):
    template_name = 'main/about.html'

    def get(self, request):
        form = FeaturesForm()
        data = {
            'form': form,
        }
        return render(request, self.template_name, data)

    def post(self, request):
        form = FeaturesForm(request.POST)
        if form.is_valid():
            solver = form.cleaned_data["solverLR"]
            max_iter = form.cleaned_data["max_iter"]
            random_state = form.cleaned_data["random_state"]
            regularization = form.cleaned_data["regularization"]
            LogR = LogisticRegression(random_state=random_state, max_iter=max_iter, solver=solver,
                                      C=regularization).fit(X_train, y_train)
            y_prediction = LogR.predict(X_valid)
            args = {
                'form': form,
                'scoretrain': float('{:.4f}'.format(LogR.score(X_train, y_train))),
                'scorevalid': float('{:.4f}'.format(LogR.score(X_valid, y_valid))),
                'precision': float('{:.4f}'.format(precision_score(y_valid, y_prediction))),
                'recall': float('{:.4f}'.format(recall_score(y_valid, y_prediction))),
                'f1': float('{:.4f}'.format(f1_score(y_valid, y_prediction)))
            }
            return render(request, self.template_name, args)


class TreeView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=8, min_samples_split=2)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_valid)
        data = [
            float('{:.4f}'.format(clf.score(X_train, y_train))),
            float('{:.4f}'.format(clf.score(X_valid, y_valid))),
            float('{:.4f}'.format(precision_score(y_valid, y_pred))),
            float('{:.4f}'.format(recall_score(y_valid, y_pred))),
            float('{:.4f}'.format(f1_score(y_valid, y_pred)))
        ]
        print(data)
        return render(request, self.template_name, {'data': data})


class ForestView(TemplateView):
    template_name = 'main/forest.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        forest = RandomForestClassifier(max_depth=8, random_state=152, min_samples_split=8, n_estimators=300)
        forest.fit(X_train, y_train)
        y_pred_forest = forest.predict(X_valid)
        data = [
            float('{:.4f}'.format(forest.score(X_train, y_train))),
            float('{:.4f}'.format(forest.score(X_valid, y_valid))),
            float('{:.4f}'.format(precision_score(y_valid, y_pred_forest))),
            float('{:.4f}'.format(recall_score(y_valid, y_pred_forest))),
            float('{:.4f}'.format(f1_score(y_valid, y_pred_forest)))
        ]
        return render(request, self.template_name, {'data': data})


class knieghView(TemplateView):
    template_name = 'main/kneigh.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        neigh = KNeighborsClassifier(n_neighbors=64, weights='uniform', algorithm='brute', p=1)
        neigh.fit(X_train, y_train)
        y_pred = neigh.predict(X_valid)
        data = [
            float('{:.4f}'.format(neigh.score(X_train, y_train))),
            float('{:.4f}'.format(neigh.score(X_valid, y_valid))),
            float('{:.4f}'.format(precision_score(y_valid, y_pred))),
            float('{:.4f}'.format(recall_score(y_valid, y_pred))),
            float('{:.4f}'.format(f1_score(y_valid, y_pred)))
        ]
        print(data)
        return render(request, self.template_name, {'data': data})


class LDAView(TemplateView):
    template_name = 'main/LDA.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        LDA = LinearDiscriminantAnalysis(solver='svd', store_covariance=True)
        LDA.fit(X_train, y_train)
        y_pred = LDA.predict(X_valid)
        data = [
            float('{:.4f}'.format(LDA.score(X_train, y_train))),
            float('{:.4f}'.format(LDA.score(X_valid, y_valid))),
            float('{:.4f}'.format(precision_score(y_valid, y_pred))),
            float('{:.4f}'.format(recall_score(y_valid, y_pred))),
            float('{:.4f}'.format(f1_score(y_valid, y_pred)))
        ]
        print(data)
        return render(request, self.template_name, {'data': data})
