import os

import matplotlib.pyplot as plt
import pandas as pd

# 创建输出文件夹
os.makedirs("output", exist_ok=True)

# 1. 读取数据
df = pd.read_csv("test.csv")

# 2. 查看数据
print("前五行数据：")
print(df.head())

print("\n数据基本信息：")
df.info()

print("\n数据统计信息：")
print(df.describe())

print("\n缺失值统计：")
print(df.isnull().sum())

# 3. 清洗数据
df = df.drop_duplicates()

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())
df["Cabin"] = df["Cabin"].fillna("Unknown")
df["Embarked"] = df["Embarked"].fillna("Unknown")

# 4. 条件筛选：保留票价大于 0 的乘客
clean_df = df[df["Fare"] > 0]

# 5. 分组统计
summary = clean_df.groupby("Sex").agg(
    人数=("PassengerId", "count"),
    平均年龄=("Age", "mean"),
    平均票价=("Fare", "mean")
)

print("\n按性别分组统计：")
print(summary)

# 6. 保存清洗后的数据
clean_df.to_csv("output/cleaned_data.csv", index=False, encoding="utf-8-sig")
summary.to_csv("output/sex_summary.csv", encoding="utf-8-sig")

# 图 1：柱状图，性别人数
plt.figure(figsize=(6, 4))
clean_df["Sex"].value_counts().plot(kind="bar", color=["skyblue", "pink"])
plt.title("Passenger Count by Sex")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output/01_sex_bar.png")
plt.close()

# 图 2：水平柱状图，登船港口人数
plt.figure(figsize=(6, 4))
clean_df["Embarked"].value_counts().plot(kind="barh", color="orange")
plt.title("Passenger Count by Embarked")
plt.xlabel("Count")
plt.ylabel("Embarked")
plt.tight_layout()
plt.savefig("output/02_embarked_barh.png")
plt.close()

# 图 3：饼图，舱位等级人数占比
plt.figure(figsize=(6, 6))
clean_df["Pclass"].value_counts().sort_index().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Pclass Percentage")
plt.ylabel("")
plt.tight_layout()
plt.savefig("output/03_pclass_pie.png")
plt.close()

# 图 4：直方图，年龄分布
plt.figure(figsize=(7, 4))
plt.hist(clean_df["Age"], bins=20, color="steelblue", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output/04_age_histogram.png")
plt.close()

# 图 5：直方图，票价分布
plt.figure(figsize=(7, 4))
plt.hist(clean_df["Fare"], bins=20, color="gold", edgecolor="black")
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output/05_fare_histogram.png")
plt.close()

# 图 6：折线图，不同舱位等级的平均票价
plt.figure(figsize=(6, 4))
average_fare = clean_df.groupby("Pclass")["Fare"].mean().sort_index()
plt.plot(average_fare.index, average_fare.values, marker="o", color="red")
plt.title("Average Fare by Pclass")
plt.xlabel("Pclass")
plt.ylabel("Average Fare")
plt.xticks([1, 2, 3])
plt.grid()
plt.tight_layout()
plt.savefig("output/06_average_fare_line.png")
plt.close()

# 图 7：散点图，年龄和票价的关系
plt.figure(figsize=(7, 4))
plt.scatter(clean_df["Age"], clean_df["Fare"], alpha=0.6, color="green")
plt.title("Age and Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.tight_layout()
plt.savefig("output/07_age_fare_scatter.png")
plt.close()

# 图 8：箱线图，不同性别的年龄比较
plt.figure(figsize=(6, 4))
male_age = clean_df[clean_df["Sex"] == "male"]["Age"]
female_age = clean_df[clean_df["Sex"] == "female"]["Age"]
plt.boxplot([male_age, female_age], tick_labels=["Male", "Female"])
plt.title("Age by Sex")
plt.ylabel("Age")
plt.tight_layout()
plt.savefig("output/08_age_boxplot.png")
plt.close()

# 图 9：堆叠柱状图，不同舱位的男女数量
plt.figure(figsize=(7, 4))
sex_pclass = pd.crosstab(clean_df["Pclass"], clean_df["Sex"])
sex_pclass.plot(kind="bar", stacked=True, ax=plt.gca())
plt.title("Sex Count by Pclass")
plt.xlabel("Pclass")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output/09_stacked_bar.png")
plt.close()

# 图 10：折线图，同船兄弟姐妹或配偶人数分布
plt.figure(figsize=(7, 4))
sibsp_count = clean_df["SibSp"].value_counts().sort_index()
plt.plot(sibsp_count.index, sibsp_count.values, marker="o", color="purple")
plt.title("SibSp Distribution")
plt.xlabel("Sibling / Spouse Count")
plt.ylabel("Passenger Count")
plt.grid()
plt.tight_layout()
plt.savefig("output/10_sibsp_line.png")
plt.close()
