<main class="form-signin">
      {% if messages %}
        {% for message in messages %}
          <div class="alert alert-{{ message.tags }}">{{ message }}</div>
        {% endfor %}
      {% endif %}
      <form method="post">
        {% csrf_token %}
        <h1 class="h3 mb-3 fw-normal">Enter Credentials</h1>
        <div class="form-floating">
          <input type="text" class="form-control" id="floatingInput" name="username" placeholder="username">
          <label for="floatingInput">Username</label>
        </div>
        <div class="form-floating">
          <input type="password" class="form-control" id="floatingPassword" name="password" placeholder="password">
          <label for="floatingPassword">Password</label>
        </div>
        <button class="w-30 btn btn-lg btn-primary" type="submit">Login</button>
      </form>
    </main>

    <div>
      <h2><b>Don't Have An Account Yet? Please Register Now</b></h2>
    </div>