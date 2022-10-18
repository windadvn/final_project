select date_transaction , sum(amount_transaction) as amount
from bigdata_transaction 
group by date_transaction 