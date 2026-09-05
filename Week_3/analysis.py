import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
n = 12000
regions = np.array(['North','South','East','West','Central'])
transport = np.array(['Road','Rail','Air','Sea'])
region = np.random.choice(regions, n, p=[.22,.20,.18,.20,.20])
mode = np.random.choice(transport, n, p=[.58,.17,.15,.10])
volume = np.clip(np.random.gamma(4.2, 23, n) + np.where(mode=='Sea',80,0) + np.where(mode=='Rail',35,0), 5, None)
distance = np.clip(np.random.lognormal(np.log(380), .65, n), 30, 2500)
rate = np.select([mode=='Air',mode=='Sea',mode=='Rail'],[5.8,1.35,2.15],default=3.1)
cost = np.clip(110 + distance*rate + volume*np.where(mode=='Air',5.5,1.65) + np.random.normal(0,180,n),150,None)
mode_days = np.select([mode=='Air',mode=='Sea',mode=='Rail'],[.8,4.8,2.9],default=2.0)
region_delay = np.select([region=='North',region=='South',region=='East',region=='West'],[.35,.10,.70,.20],default=.25)
delivery = np.clip(.9 + distance/250 + mode_days + region_delay + np.random.gamma(2,.7,n) + np.random.normal(0,.9,n),1,None)
estimated = delivery + np.random.normal(.7,1.8,n)
late = (delivery > estimated).astype(int)
fuel = np.clip(distance*np.where(mode=='Air',.42,np.where(mode=='Sea',.10,np.where(mode=='Rail',.16,.24))) + np.random.normal(0,35,n),20,None)
satisfaction = np.clip(5 - .18*np.maximum(delivery-4,0) - .0008*np.maximum(cost-1800,0) + np.random.normal(0,.35,n),1,5)

df = pd.DataFrame({'shipment_id':range(1,n+1),'region':region,'transport_mode':mode,'shipment_volume_kg':volume,'distance_km':distance,'transport_cost':cost,'delivery_time_days':delivery,'estimated_delivery_days':estimated,'late_flag':late,'fuel_cost':fuel,'customer_satisfaction':satisfaction})

print(df.describe().T)
print(f'Late rate: {df.late_flag.mean()*100:.2f}%')
print(f'On-time rate: {(1-df.late_flag.mean())*100:.2f}%')
print(f'Average delivery: {df.delivery_time_days.mean():.2f} days')
print(f'Median delivery: {df.delivery_time_days.median():.2f} days')
print(f'Average transport cost: {df.transport_cost.mean():.2f}')

mode_summary = df.groupby('transport_mode').agg(shipments=('shipment_id','count'),avg_delivery_days=('delivery_time_days','mean'),avg_cost=('transport_cost','mean'),late_rate=('late_flag','mean'))
mode_summary['late_rate'] *= 100
print('\nBy transport mode:\n', mode_summary)

region_summary = df.groupby('region').agg(shipments=('shipment_id','count'),avg_delivery_days=('delivery_time_days','mean'),avg_cost=('transport_cost','mean'),late_rate=('late_flag','mean'))
region_summary['late_rate'] *= 100
print('\nBy region:\n', region_summary.sort_values('late_rate',ascending=False))

corr = df[['shipment_volume_kg','distance_km','transport_cost','delivery_time_days','fuel_cost','customer_satisfaction']].corr()
print('\nCorrelation with cost:\n', corr['transport_cost'].drop('transport_cost').sort_values(key=np.abs,ascending=False))

plt.hist(df.delivery_time_days,bins=35)
plt.xlabel('Delivery time (days)'); plt.ylabel('Shipments'); plt.title('Distribution of Delivery Time')
plt.tight_layout(); plt.savefig('delivery_time_distribution.png',dpi=180); plt.close()

mode_summary.avg_delivery_days.sort_values().plot(kind='bar')
plt.ylabel('Average delivery time (days)'); plt.title('Average Delivery Time by Transport Mode'); plt.tight_layout(); plt.savefig('delivery_by_mode.png',dpi=180); plt.close()

plt.scatter(df.distance_km.sample(2500,random_state=42),df.transport_cost.loc[df.distance_km.sample(2500,random_state=42).index],s=8,alpha=.35)
plt.xlabel('Distance (km)'); plt.ylabel('Transportation cost'); plt.title('Transportation Cost vs Distance'); plt.tight_layout(); plt.savefig('cost_vs_distance.png',dpi=180); plt.close()

region_summary.late_rate.sort_values().plot(kind='barh')
plt.xlabel('Late shipment rate (%)'); plt.title('Late Shipment Rate by Region'); plt.tight_layout(); plt.savefig('late_rate_region.png',dpi=180); plt.close()
