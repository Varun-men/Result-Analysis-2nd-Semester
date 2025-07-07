import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("figures", exist_ok=True)

df = pd.read_csv("results.csv")
print(df.head())
df.info()
df.columns

subjects = [
    'AC_TOTAL','AP-2_TOTAL','AM-2_TOTAL','ES_TOTAL','EM_TOTAL','IC_TOTAL','HV_TOTAL','AC-LAB_TOTAL','AP-LAB_TOTAL','ES-LAB_TOTAL',
    'EG-LAB_TOTAL','Workshop_TOTAL'
]


for subject in subjects:
    max_marks = df[subject].max()
    min_marks = df[subject].min()
    
    toppers = df.loc[df[subject] == max_marks, 'Name'].values
    lowest_scorers = df.loc[df[subject] == min_marks, 'Name'].values
    
    print(f"\n📚 {subject}:")
    print(f"🏆 Topper(s): {', '.join(toppers)} with {max_marks} marks")
    print(f"❌ Lowest scorer(s): {', '.join(lowest_scorers)} with {min_marks} marks")


max_sgpa = df['SGPA'].max()
sgpa_toppers = df.loc[df['SGPA'] == max_sgpa, 'Name'].values
print(f"\n⭐ Highest SGPA: {', '.join(sgpa_toppers)} with SGPA {max_sgpa}")


min_sgpa = df['SGPA'].min()
sgpa_losers = df.loc[df['SGPA'] == min_sgpa, 'Name'].values
print(f"💀 Lowest SGPA: {', '.join(sgpa_losers)} with SGPA {min_sgpa}")


sub = [
    'AC',
    'AP-2',
    'AM-2',
    'ES',
    'EM',
    'IC',
    'HV',
    'AP-LAB',
    'AC-LAB',
    'ES-LAB',
    'EG-LAB',
    'Workshop'
]


for subject in sub:
    x = np.arange(len(df['Name']))
    plt.figure(figsize=(14, 6))
    width = 0.22

    # Custom colors
    colors = ['#4285F4', '#DB4437', '#F4B400']

    # Plotting Bars
    bars1 = plt.bar(x - width, df[f'{subject}_INT'], width, label='Internal', color=colors[0],edgecolor='black')
    bars2 = plt.bar(x, df[f'{subject}_EXT'], width, label='External', color=colors[1],edgecolor='black')
    bars3 = plt.bar(x + width, df[f'{subject}_TOTAL'], width, label='Total', color=colors[2],edgecolor='black')

    # Titles and labels
    plt.xlabel('Student Name', fontsize=12,weight='bold')
    plt.ylabel('Marks', fontsize=12,weight='bold')
    plt.title(f'{subject.replace("_", " ")} Marks Distribution', fontsize=14, weight='bold', pad=15)
    plt.xticks(x, df['Name'], fontsize=11)
    plt.yticks(fontsize=11)

    plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

    for bar_group in [bars1, bars2, bars3]:
        for bar in bar_group:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{height:.0f}', ha='center', fontsize=9,weight='bold')

    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.savefig(f"figures-1R/{subject}_marks_distribution.png", dpi=300, bbox_inches='tight')
    plt.show()



# # 3️⃣ Subject Difficulty Analysis
# print("🎯 Subject-wise Average Marks:")
# subject_averages = {}

# for subject in subjects:
#     avg_marks = df[subject].mean()
#     subject_averages[subject] = avg_marks
#     print(f"{subject}: {avg_marks:.2f}")


# lowest_avg_subject = min(subject_averages, key=subject_averages.get)
# lowest_avg_value = subject_averages[lowest_avg_subject]

# highest_avg_subject = max(subject_averages, key=subject_averages.get)
# highest_avg_value = subject_averages[highest_avg_subject]

# print(f"\n💀 Subject with Lowest Average Marks: {lowest_avg_subject} ({lowest_avg_value:.2f} marks)")
# print(f"🏆 Subject with Highest Average Marks: {highest_avg_subject} ({highest_avg_value:.2f} marks)")
# avg_marks_list = list(subject_averages.values())

# x = np.arange(len(subjects))

# plt.figure(figsize=(14, 7))
# bars = plt.bar(x, avg_marks_list, color='#34A853',edgecolor='black')

# plt.xlabel('Subjects', fontsize=12,weight='bold')
# plt.ylabel('Average Marks', fontsize=12,weight='bold')
# plt.title('Subject-wise Average Total Marks', fontsize=14, weight='bold',pad=15)
# plt.xticks(x, subjects, rotation=45, ha='right', fontsize=10)
# plt.yticks(fontsize=11)

# for bar in bars:
#     height = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, f'{height:.1f}', ha='center', fontsize=9,weight='bold')

# plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
# plt.tight_layout()
# plt.savefig("figure-2R.png", dpi=300, bbox_inches='tight')
# plt.show()



# #(subject with highest variance = most unpredictable)
# print("\n🎯 Subject-wise Standard Deviation:")
# subject_stddevs = {}

# for subject in subjects:
#     stddev_marks = df[subject].std()
#     subject_stddevs[subject] = stddev_marks
#     print(f"{subject}: {stddev_marks:.2f}")

# highest_std_subject = max(subject_stddevs, key=subject_stddevs.get)
# highest_std_value = subject_stddevs[highest_std_subject]
# print(f"\n📈 Subject with Highest Standard Deviation: {highest_std_subject} ({highest_std_value:.2f})")

# lowest_std_subject = min(subject_stddevs, key=subject_stddevs.get)
# lowest_std_value = subject_stddevs[lowest_std_subject]
# print(f"📉 Subject with Lowest Standard Deviation: {lowest_std_subject} ({lowest_std_value:.2f}\n)")
# stddevs_value = list(subject_stddevs.values())
# x = np.arange(len(subjects))

# plt.figure(figsize=(14, 7))
# bars = plt.bar(x, stddevs_value, color='#FBBC05',edgecolor='black')

# plt.xlabel('Subjects', fontsize=12,weight='bold')
# plt.ylabel('Standard Deviation', fontsize=12,weight='bold')
# plt.title('Subject-wise Standard Deviation of Total Marks', fontsize=14, weight='bold',pad=15)
# plt.xticks(x, subjects, rotation=45, ha='right', fontsize=10)
# plt.yticks(fontsize=11)

# for bar in bars:
#     height = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, height + 0.3, f'{height:.2f}', ha='center', fontsize=9,weight='bold')

# plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
# plt.tight_layout()
# plt.savefig("figure-3R.png", dpi=300, bbox_inches='tight')
# plt.show()


# subjec = [
#     'AC',
#     'AP-2',
#     'AM-2',
#     'ES',
#     'EM',
#     'IC',
#     'HV',
#     'AC-LAB',
#     'AP-LAB',
#     'ES-LAB',
#     'EG-LAB',
#     'Workshop'
# ]

# # 🎯 Internal vs External Average Marks per Subject
# internal_averages = []
# external_averages = []

# for subject in subjec:
#     internal_avg = df[f'{subject}_INT'].mean()
#     external_avg = df[f'{subject}_EXT'].mean()
#     internal_averages.append(internal_avg)
#     external_averages.append(external_avg)
#     print(f"{subject}: Internal Avg = {internal_avg:.2f}, External Avg = {external_avg:.2f}")


# x = np.arange(len(subjects))
# width = 0.35
# plt.figure(figsize=(14, 7))
# bars1 = plt.bar(x - width/2, internal_averages, width, label='Internal Avg', color='#4285F4',edgecolor='black')
# bars2 = plt.bar(x + width/2, external_averages, width, label='External Avg', color='#DB4437',edgecolor='black')
# plt.xlabel('Subjects', fontsize=12,weight='bold')
# plt.ylabel('Average Marks', fontsize=12,weight='bold')
# plt.title('Internal vs External Average Marks Comparison', fontsize=14, weight='bold',pad=15)
# plt.xticks(x, [sub.replace("_", " ") for sub in subjects],rotation = 45, ha='right', fontsize=10)
# plt.yticks(fontsize=11)

# for bar_group in [bars1, bars2]:
#     for bar in bar_group:
#         height = bar.get_height()
#         plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, f'{height:.1f}', ha='center', fontsize=9,weight='bold')

# plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
# plt.legend(fontsize=11)
# plt.tight_layout()
# plt.savefig("figure-4R.png", dpi=300, bbox_inches='tight')
# plt.show()




# bins = [6.0, 7.0, 8.0, 9.0, 10.0]
# labels = ['6.0-7.0', '7.0-8.0', '8.0-9.0', '9.0-10.0']

# df['SGPA_Category'] = pd.cut(df['SGPA'], bins=bins, labels=labels, right=False)

# sgpa_distribution = df['SGPA_Category'].value_counts().sort_index()
# plt.figure(figsize=(8,5))
# bars = plt.bar(sgpa_distribution.index, sgpa_distribution.values, color='#DB4437',edgecolor='black')
# plt.title('SGPA Distribution of Students', fontsize=14, weight='bold',pad=15)
# plt.xlabel('SGPA Range', fontsize=12,weight='bold')
# plt.ylabel('Number of Students', fontsize=12,weight='bold')
# plt.xticks(fontsize=11)
# plt.yticks(fontsize=11)

# for bar in bars:
#     height = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, f'{int(height)}', ha='center', fontsize=10,weight='bold')

# plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
# plt.tight_layout()
# plt.savefig("figure-5R.png", dpi=300, bbox_inches='tight')
# plt.show()





# #Credit Weighted Percentage Analysis
# credits = {
#     'AC': 3,
#     'AP-2': 3,
#     'AM-2': 4,
#     'ES': 3,
#     'EM': 3,
#     'IC': 2,
#     'Workshop': 2,
#     'HV': 1,
#     'AC-LAB': 1,
#     'AP-LAB': 1,
#     'ES-LAB': 1,
#     'EG-LAB': 1
# }

# total_credits = sum(credits.values())

# def calculate_credit_weighted_percentage(row):
#     weighted_sum = 0
#     for subject, credit in credits.items():
#         weighted_sum += row[f'{subject}_TOTAL'] * credit
#     equivalent_percent = weighted_sum / total_credits
#     return equivalent_percent

# df['Credit_Weighted_Percentage'] = df.apply(calculate_credit_weighted_percentage, axis=1)

# result_df = df[['Name', 'SGPA', 'Percentage', 'Credit_Weighted_Percentage']]
# print(result_df)

# x = np.arange(len(df['Name']))
# plt.figure(figsize=(12, 7))
# bar_width = 0.35
# bars1 = plt.bar(x - bar_width/2, df['Percentage'], width=bar_width, label='Official Percentage', color='#34A853', edgecolor='black')
# bars2 = plt.bar(x + bar_width/2, df['Credit_Weighted_Percentage'], width=bar_width, label='Credit Weighted Percentage', color='#4285F4', edgecolor='black')
# plt.xlabel('Students', fontsize=14, weight='bold')
# plt.ylabel('Percentage (%)', fontsize=14, weight='bold')
# plt.title('Official Percentage vs Credit Weighted Percentage', fontsize=16, weight='bold', pad=15)
# plt.xticks(x, df['Name'], fontsize=12)
# plt.ylim(50, 100)

# for bar in bars1:
#     height = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, f'{height:.2f}%', ha='center', fontsize=11, weight='bold')

# for bar in bars2:
#     height = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, f'{height:.2f}%', ha='center', fontsize=11, weight='bold')

# plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.6)
# plt.legend(fontsize=12, loc='upper left')
# plt.tight_layout()
# plt.savefig("figure-6R.png", dpi=300, bbox_inches='tight')
# plt.show()