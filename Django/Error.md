# Error

### form 만들어주면됨

![](Error_assets/2023-03-23-09-26-02-image.png)

사이트 만들고 게시글 추가했을때 : migrations 해줘야됨

![](Error_assets/2023-03-24-09-36-31-image.png)

migrate

![](Error_assets/2023-03-24-16-41-16-image.png)

들여쓰기 하니까 고쳐졌는데 그냥 문법적으로 틀린건가 머징?

![](Error_assets/2023-03-24-16-45-17-image.png)

base.html

```html
{% load static %}
```

![](Error/2023-03-25-14-31-38-image.png)

```html
<a href="{% url 'movies:index' %}">BACK</a>
```

![](Error/2023-03-25-15-00-59-image.png)

![](Error/2023-03-26-15-34-23-image.png)
