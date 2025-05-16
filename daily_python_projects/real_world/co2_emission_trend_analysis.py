import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def load_data(file_name):
    """Load CO2 data from a CSV file."""
    return  pd.read_csv(file_name)

def clean_data(df):
    """Clean and preprocess the data."""
    # Convert 'Year' and 'Month' to a 'Date' column
    df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))
    return df

def plot_trends(df):
    """Plot CO2 levels over time."""
    plt.figure(figsize=(10,6))
    sns.lineplot(x='Date', y='CO2_Level', data=df)
    plt.title('CO2 Levels Over Time (Mauna Loa)')
    plt.xlabel('Year')
    plt.ylabel('CO2 Concentration (ppm)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def calculate_statistics(df):
    """Calculate and display basic statistics."""
    avg_co2 = df['CO2_Level'].mean()
    max_co2 = df['CO2_Level'].max()
    min_co2 = df['CO2_Level'].min()

    print(f"Average CO2 Level: {avg_co2:.2f} ppm")
    print(f"Maximum CO2 Level: {max_co2:.2f} ppm")
    print(f"Minimum CO2 Level: {min_co2:.2f} ppm")

def main():
    # Load and clean the data
    df = load_data('co2.csv')
    df = clean_data(df)

    # Plot the CO2 levels
    plot_trends(df)

    # Calculate and display basic statistics
    calculate_statistics(df)

if __name__ == "__main__":
    main()



