import seaborn as sns   


def violin_plot(x_label, y_label, string, dados_plot):
    return sns.violinplot(x = x_label, y = y_label, hue = string, data = dados_plot)