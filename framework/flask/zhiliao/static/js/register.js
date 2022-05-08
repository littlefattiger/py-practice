function bindCaptchaBtnClick() {
    $("#button-addon2").on("click", function (event) {
        var $this = $(this)
        var email = $("input[name='email']").val();
        if (!email) {
            alert("请输入邮箱")
            return;
        }
        $.ajax({
            url: "captcha",
            method: "POST",
            data: {
                "email": email
            },
            success: function (res) {
                var code = res['code'];
                if (code === 200) {
                    $this.off("click")
                    var countDown = 60;
                    var timer = setInterval(function () {
                        countDown -= 1;
                        if (countDown > 0) {
                            $this.text(countDown + "秒后重新发送");
                        } else {
                            $this.text("获取验证码");
                            bindCaptchaBtnClick();
                            clearInterval(timer);
                        }

                    }, 1000);

                    alert("验证发发送成功")
                } else {
                    alert(res['message'])
                }
            }
        })
    })
}

$(function () {
        bindCaptchaBtnClick();
    }
)