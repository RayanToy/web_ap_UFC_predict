from django.db import models

class features(models.Model):
    criterion_choises = [
        ("gini","gini"),
        ("entropy","entropy"),
        ("log_loss","log_loss")
                ]
    solver_choises_LR = [
        ("lbfgs", "lbfgs"),
        ("liblinear", "liblinear"),
        ("newton-cg", "newton-cg"),
        ("newton-cholesky", "newton-cholesky"),
        ("sag", "sag"),
        ("saga", "saga"),
                     ]
    solver_choises_LDA = [
        ("svd", "svd"),
        ("lsqr", "lsqr"),
        ("eigen", "eigen")
                        ]
    weights_choises = [
        ("uniform", "uniform"),
        ("distance", "distance"),
                        ]
    algorithm_choises = [
        ("auto", "auto"),
        ("ball_tree", "ball_tree"),
        ("kd_tree", "kd_tree"),
        ("brute", "brute")
                        ]
    criterion = models.CharField("Критерий", max_length=8, choices=criterion_choises, default='entropy')
    max_depth = models.IntegerField('Глубина дерева')
    min_samples_split = models.IntegerField('Минимум образцов для разделения узла')
    min_samples_leaf = models.IntegerField('Минимум образцов для терминального узла')

    solverLR = models.CharField('Решатель',max_length=15, choices=solver_choises_LR, default='lbfgs')
    max_iter = models.IntegerField('Максимальное количество итераций')
    random_state = models.IntegerField('Показатель случайности выборки')
    regularization = models.FloatField('Регуляризация')

    solverLD = models.CharField('Решатель',  max_length=5, choices=solver_choises_LDA, default='svd')
    covariance_estimator = models.BooleanField('Ковариационный оценщик', default=True)
    shrinkage = models.IntegerField('Влияние выборки', default=None)
    tol = models.IntegerField('Погрешность')

    random_state_forest = models.IntegerField("Показатель случайности выборки")
    max_depth_forest = models.IntegerField('Максимальная глубина деревьев')
    n_estimators = models.IntegerField('Количество')
    min_samples_split_forest = models.IntegerField('Минимум образцов для разделения узла')

    n_neighbors = models.IntegerField("Количество соседей")
    weights = models.CharField('Весовая функция',  max_length=8, choices=weights_choises, default='uniform')
    algorithm = models.CharField('Алгоритм', max_length=9, choices=algorithm_choises, default='auto')
    p = models.IntegerField("Мощность Минковского")


    class Meta:
        verbose_name = 'Набор признаков боя'
        verbose_name_plural = 'Наборы признаков боя'

    def __str__(self):
        return "Бой"
