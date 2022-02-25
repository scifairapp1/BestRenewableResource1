
x = [[], [], [], [], [], [], [], []]
y = []
x, y = array(x), array(y)
>>> print(x)
[[]
[]
[]
[]
[]
[]
[]
[]]
>>> print(y)
[]
[]
[]
[]
[]
[]
[]
[]
model = LinearRegression().fit(x, y, z,)
>>> r_sq = model.score(x, y)
>>> print('coefficient of determination:', r_sq)
coefficient of determination: 0.8615939258756776
>>> print('intercept:', model.intercept_)
intercept: 5.52257927519819
>>> print('slope:', model.coef_)
slope: [0.44706965 0.25502548]
>>> y_pred = model.predict(x)
>>> print('predicted response:', y_pred, sep='\n')
predicted response:
 38.78227633 41.27265006]
>>> y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1)
>>> print('predicted response:', y_pred, sep='\n')
predicted response:
[]
>>> x_new = np.arange(10).reshape((-1, 2))
>>> print(x_new)
[[0 1]
[2 3]
[4 5]
[6 7]
[8 9]]
>>> y_new = model.predict(x_new)
>>> print(y_new)
[5.77760476  7.18179502  8.58598528  9.99017554 11.3943658]