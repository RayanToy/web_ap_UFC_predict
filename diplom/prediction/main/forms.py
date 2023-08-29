from .models import features
from django.forms import ModelForm, Select, NumberInput

class FeaturesForm(ModelForm):
    class Meta:
        model = features
        fields = ["criterion", "max_depth", "min_samples_split", "min_samples_leaf", "solverLR", "max_iter", "random_state", "regularization",
                  "solverLD", "covariance_estimator", "shrinkage", "tol", "random_state_forest", "max_depth_forest", "n_estimators", "min_samples_split_forest",
                  "n_neighbors", "weights", "algorithm", "p"
                  ]
        widgets = {
            "solverLR": Select(attrs=
            {
                'class': 'form-control',
                'placeholder': 'Решатель'
            }),
            "max_iter": NumberInput(attrs=
            {
                'class': 'form-control',
                'placeholder': 'Максимальное количество итераций'
            }),
            "random_state": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Показатель случайности выборки'
            }),
            "regularization": NumberInput(attrs=
            {
                'class': 'form-control',
                'placeholder': 'Регуляризация'
            })
        }
