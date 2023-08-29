from django.views.generic import TemplateView
from .models import UFC_data
from .forms import UFC_data_Form
from django.shortcuts import render
from sklearn import tree
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier

ufc_data = pd.read_csv(r"D:\Загрузки\Ufc_Dt (1).csv")
ufc_data.drop("Unnamed: 0", axis=1, inplace=True)
label = ufc_data.Winner
ufc_data = ufc_data.drop('Winner', axis=1)
X_train, X_valid, y_train, y_valid = train_test_split(ufc_data, label, random_state=0, test_size=0.3)


def form(request):
    UFC = UFC_data.objects.all()
    return render(request, "forms/form.html", {"UFC": UFC})


class HomeView(TemplateView):
    template_name = 'forms/predict.html'

    def get(self, request):
        form = UFC_data_Form()
        data = {
            'form': form,
        }
        return render(request, self.template_name, data)

    def post(self, request):
        form = UFC_data_Form(request.POST)
        if form.is_valid():
            value1 = form.cleaned_data["win_streak_dif"]
            value2 = form.cleaned_data["longest_win_streak_dif"]
            value3 = form.cleaned_data["loss_dif"]
            value4 = form.cleaned_data["age_dif"]
            value5 = form.cleaned_data["avg_td_dif"]
            value6 = form.cleaned_data["draw_diff"]
            value7 = form.cleaned_data["win_by_Decision_Split_diff"]
            value8 = form.cleaned_data["win_by_Decision_Unanimous_diff"]
            value9 = form.cleaned_data["win_by_TKO_Doctor_Stoppage_diff"]
            value10 = form.cleaned_data["odds_diff"]
            value11 = form.cleaned_data["ev_diff"]
            value12 = form.cleaned_data["kd_bout_diff"]
            value13 = form.cleaned_data["tot_str_landed_bout_diff"]
            value14 = form.cleaned_data["tot_str_attempted_bout_diff"]
            value15 = form.cleaned_data["td_landed_bout_diff"]
            value16 = form.cleaned_data["td_attempted_bout_diff"]
            value17 = form.cleaned_data["td_pct_bout_diff"]
            value18 = form.cleaned_data["sub_attempts_bout_diff"]
            value19 = form.cleaned_data["pass_bout_diff"]
            value20 = form.cleaned_data["rev_bout_diff"]
            clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=8, min_samples_split=2)
            clf.fit(X_train, y_train)
            LDA = LinearDiscriminantAnalysis(solver='svd', store_covariance=True, covariance_estimator=None)
            LDA.fit(X_train, y_train)
            forest = RandomForestClassifier(max_depth=8, random_state=152, min_samples_split=8, n_estimators=300)
            forest.fit(X_train, y_train)
            LogR = LogisticRegression(random_state=0, max_iter=394, solver='newton-cg').fit(X_train, y_train)
            neigh = KNeighborsClassifier(n_neighbors=64, weights='uniform', algorithm='brute', p=1)
            neigh.fit(X_train, y_train)
            features = np.array([[value1, value2, value3, value4, value5, value6, value7, value8, value9, value10,
                                  value11, value12, value13, value14, value15, value16, value17, value18, value19,
                                  value20]])
            clf_prediction = clf.predict_proba(features)
            LogR_prediction = LogR.predict_proba(features)
            forest_prediction = forest.predict_proba(features)
            neigh_prediction = neigh.predict_proba(features)
            LDA_prediction = LDA.predict_proba(features)
            args = {'form': form,
                    "clf_prediction": float('{:.3f}'.format(clf_prediction[0][1])),
                    "LogR_prediction": float('{:.3f}'.format(LogR_prediction[0][1])),
                    "forest_prediction": float('{:.3f}'.format(forest_prediction[0][1])),
                    "neigh_prediction": float('{:.3f}'.format(neigh_prediction[0][1])),
                    "LDA_prediction": float('{:.3f}'.format(LDA_prediction[0][1]))
                    }
            return render(request, self.template_name, args)
