document.addEventListener('DOMContentLoaded', function() {
    // 페이지가 로드되면 로그인 폼을 불러옵니다.
    loadLoginForm();
});

function loadLoginForm() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'login.html', true);
    xhr.onreadystatechange = function() {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            // 요청이 성공적으로 완료되면, 로그인 폼의 HTML을 페이지에 삽입합니다.
            document.getElementById('login-form-container').innerHTML = this.responseText;
        }
    };
    xhr.send();
}
