X = rep(0, 100)
p = 0.38
cumul = 0
for (i in 1:1000){
  try = 0
  while (cumul < 5){
    if (runif(1)<p) cumul = cumul + 1
    else cumul = 0
    try = try + 1
  }
  X[i] = try
  cumul = 0
}
mean(X) * 250
max(X)
min(X)

Y = rep(0,10000)
p2 = 0.003 #0.3 1.3 0.8
get = 0
for (j in 1:10000){
  try = 0
  while (get == 0){
    if (runif(1)<p2) get = 1
    try = try + 1
  } 
  Y[j] = try
  get = 0
}
Y
mean(Y)
min(Y)
max(Y)

newspaper = read.csv('newspaper.csv')
newspaper = na.omit(newspaper)
plot(newspaper$daily, newspaper$sunday)
for (i in 1:nrow(newspaper)){
  if(newspaper[i,3]>mean(newspaper$sunday)) newspaper[i,3]=2
  else newspaper[i,3]=1
}

for (i in 1:nrow(newspaper)){
  if(newspaper[i,2]>mean(newspaper$daily)) newspaper[i,2]=2
  else newspaper[i,2]=1
}

par(mfrow=c(1:2))
hist(newspaper$daily)
hist(newspaper$sunday)
newspaper
