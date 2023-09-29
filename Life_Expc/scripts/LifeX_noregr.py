import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

file = r'C:\Users\USER\Desktop\Life_Project\Life_Expc\data\life_X_piv.csv'
df = pd.read_csv(file)
print(df)

# Convert 'Ожидаемый возраст населения при рождении' column to float
df['Ожидаемый возраст населения при рождении'] = df['Ожидаемый возраст населения при рождении'].fillna(0).astype(float)
df['Год'] = df['Год'].fillna(0).astype(int)
print(df.dtypes)

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(9, 16))

# Get unique years from the 'Год' column
years = df['Год'].unique()

def animate(year_index):
    ax.clear()
    year = years[year_index]
    filtered = df[df['Год'] == year]
    filt_areas = filtered[filtered['Регион'] != 'Республика Казахстан '].sort_values('Ожидаемый возраст населения при рождении')
    filt_areas.drop(filt_areas[filt_areas['Ожидаемый возраст населения при рождении'] == 0].index, inplace=True)
    plot = plt.barh(y=filt_areas['Регион'], width=filt_areas['Ожидаемый возраст населения при рождении'], color='#E6825D')

    ax.set_xlim(0, max(df['Ожидаемый возраст населения при рождении']))  # Adjust the limit based on your data range
    ax.bar_label(plot, padding=3, labels=[f'{value:.2f}' for value in filt_areas['Ожидаемый возраст населения при рождении']])

    for edge in ['top', 'right', 'bottom', 'left']:
        ax.spines[edge].set_visible(False)

    ax.tick_params(left=False)
    ax.get_xaxis().set_visible(False)

    ax.set_title(f'Ожидаемая продолжительность жизни по Регионам на {year} год c прогнозом  ', size=18, weight='bold')

plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'

# Define the range of years you want to animate
years_to_animate = range(len(years))
animation = FuncAnimation(fig, animate, frames=years_to_animate, interval=1000)

# Uncomment the next line if you want to save the animation as a GIF
# animation.save('population_animate.gif', dpi=100, writer=PillowWriter(fps=100))

plt.show()