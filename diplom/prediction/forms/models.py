from django.db import models

class UFC_data(models.Model):
    tot_str_landed_bout_diff = models.FloatField("Среднее количество значимых ударов за бой")
    tot_str_attempted_bout_diff = models.FloatField("Среднее количество предпринятых ударов за бой")
    ev_diff = models.FloatField("Показатель отклонения от среднего выигрыша")
    odds_diff = models.FloatField("Ставки на определенных игроков.")
    kd_bout_diff = models.FloatField("Нокдауновые бои")
    pass_bout_diff = models.FloatField("Перемещение позиции")
    td_landed_bout_diff = models.FloatField("Удачный тейдкдаун")
    td_pct_bout_diff = models.FloatField("Средняя точность тейкдаунов за бой")
    sub_attempts_bout_diff = models.FloatField("Разница подачи соперника в сдачу")
    age_dif = models.FloatField("Возраст")
    win_streak_dif = models.FloatField("Количество побед")
    td_attempted_bout_diff = models.FloatField("Попытка тейкдауна")
    win_by_Decision_Split_diff = models.FloatField("Победа раздельным решением судей")
    avg_td_dif = models.FloatField("Среднее количество тейкдаунов")
    loss_dif = models.FloatField("Вес")
    longest_win_streak_dif = models.FloatField("Наибольшее количество побед подряд")
    rev_bout_diff = models.FloatField("Оборот бойца")
    win_by_TKO_Doctor_Stoppage_diff = models.FloatField("Победа по причине остановки боя доктором")
    draw_diff = models.FloatField("Количество ничьих")
    win_by_Decision_Unanimous_diff = models.FloatField("Победа единогласным решением")

    class Meta:
        verbose_name = 'Набор признаков боя'
        verbose_name_plural = 'Наборы признаков боя'

    def __str__(self):
        return "Бой"