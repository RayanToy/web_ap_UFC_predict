from .models import UFC_data
from django.forms import ModelForm, NumberInput

class UFC_data_Form(ModelForm):
    class Meta:
        model = UFC_data
        fields = ["tot_str_landed_bout_diff","tot_str_attempted_bout_diff","ev_diff","odds_diff","kd_bout_diff","pass_bout_diff","td_landed_bout_diff",
                  "td_pct_bout_diff","sub_attempts_bout_diff",
                  "age_dif", "win_streak_dif", "td_attempted_bout_diff", "win_by_Decision_Split_diff", "avg_td_dif", "loss_dif",
                  "longest_win_streak_dif", "rev_bout_diff", "win_by_TKO_Doctor_Stoppage_diff", "draw_diff", "win_by_Decision_Unanimous_diff"]

        widgets = {
            "tot_str_landed_bout_diff": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Среднее количество значимых ударов за бой'
                                                    }),
            "tot_str_attempted_bout_diff": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Среднее количество предпринятых ударов за бой'
                                                    }),
            "ev_diff": NumberInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': 'Показатель отклонения от среднего выигрыша'
                                                    }),
            "odds_diff": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Ставки на определенных игроков'
                                                    }),
            "kd_bout_diff": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Нокдауновые бои'
                                                    }),
            "pass_bout_diff": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Перемещение позиции'
                                                    }),

            "td_landed_bout_diff": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Удачный тейдкдаун'
                                                    }),
            "td_pct_bout_diff": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Средняя точность тейкдаунов за бой'
                                                    }),
            "sub_attempts_bout_diff": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Разница подачи соперника в сдачу'
                                                    }),
            "age_dif": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Возраст'
                                                    }),
            "td_attempted_bout_diff": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Попытка тейкдауна'
                                                    }),
            "win_streak_dif": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Количество побед подряд'
                                                    }),
            "avg_td_dif": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Победа раздельным решением судей'
                                                    }),
            "win_by_Decision_Split_diff": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Среднее количество тейкдаунов'
                                                    }),
            "loss_dif": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Вес'
                                                    }),
            "longest_win_streak_dif": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Наибольшее количество побед подряд'
                                                    }),
            "rev_bout_diff": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Оборот бойца'
                                                    }),
            "win_by_TKO_Doctor_Stoppage_diff": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Победа по причине остановки боя доктором'
                                                    }),

            "draw_diff": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Количество ничьих'
                                                    }),

            "win_by_Decision_Unanimous_diff": NumberInput(attrs=
                                                    {
                                                        'class': 'form-control',
                                                        'placeholder': 'Победа единогласным решением'
                                                    })
        }
