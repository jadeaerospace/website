// Contact form (sent by FormSubmit to the inbox below; no backend needed) + copy-email button.
(function () {
  var EMAIL = 'aila@alyaspace.com';
  var zh = document.documentElement.lang.indexOf('zh') === 0;
  var T = zh
    ? { sending: '发送中…', ok: '已收到，我们会尽快回复。', err: '发送失败，请直接发邮件到 ', copied: '已复制' }
    : { sending: 'Sending…', ok: 'Thanks, we got your message and will reply soon.', err: 'Could not send. Please email ', copied: 'Copied' };

  var form = document.getElementById('contact-form');
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    var msg = form.querySelector('.form-msg'), btn = form.querySelector('button[type=submit]');
    if (form.elements._honey.value) return;
    btn.disabled = true; msg.textContent = T.sending; msg.classList.remove('err');
    fetch('https://formsubmit.co/ajax/' + EMAIL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({
        name: form.elements.name.value,
        email: form.elements.email.value,
        organisation: form.elements.org.value,
        message: form.elements.message.value,
        _subject: 'jadeaerospace.com enquiry from ' + form.elements.name.value,
        _template: 'table'
      })
    }).then(function (r) { return r.json(); }).then(function (d) {
      if (String(d.success) !== 'true') throw new Error(d.message || 'failed');
      form.reset(); msg.textContent = T.ok;
    }).catch(function () {
      msg.textContent = T.err + EMAIL; msg.classList.add('err');
    }).finally(function () { btn.disabled = false; });
  });

  document.querySelectorAll('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var label = b.textContent;
      var done = function () { b.textContent = T.copied; setTimeout(function () { b.textContent = label; }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(EMAIL).then(done, function () { window.prompt('', EMAIL); });
      else window.prompt('', EMAIL);
    });
  });
})();
