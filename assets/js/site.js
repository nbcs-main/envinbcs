/* Small progressive enhancements. The site works without this file. */
(function () {
	var btn = document.querySelector('.nav-toggle');
	var nav = document.getElementById('site-nav');
	function setOpen(open) {
		btn.setAttribute('aria-expanded', String(open));
		nav.setAttribute('data-open', String(open));
	}
	if (btn && nav) {
		btn.addEventListener('click', function () {
			setOpen(btn.getAttribute('aria-expanded') !== 'true');
		});
		document.addEventListener('keydown', function (e) {
			if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') {
				setOpen(false);
				btn.focus();
			}
		});
	}
	var year = document.getElementById('year');
	if (year) year.textContent = new Date().getFullYear();
})();
