/* Search + category filter for card grids (projects, stories).
   Cards are plain HTML, so the lists work for search engines and without JavaScript;
   this file only hides or shows them. Markup contract, inside an element with data-filter-scope:
     [data-filter-input]            search box
     [data-filter-button="value"]   category buttons ("all" shows everything)
     [data-filter-item]             each card, with data-category="..." and data-search="lowercase text"
     [data-filter-empty]            "no results" message (add the hidden attribute) */
(function () {
	document.querySelectorAll('[data-filter-scope]').forEach(function (scope) {
		var items = Array.prototype.slice.call(scope.querySelectorAll('[data-filter-item]'));
		var buttons = scope.querySelectorAll('[data-filter-button]');
		var input = scope.querySelector('[data-filter-input]');
		var empty = scope.querySelector('[data-filter-empty]');
		var active = 'all';

		function apply() {
			var q = (input && input.value || '').trim().toLowerCase();
			var shown = 0;
			items.forEach(function (item) {
				var okCategory = active === 'all' || item.getAttribute('data-category') === active;
				var okQuery = !q || (item.getAttribute('data-search') || '').indexOf(q) !== -1;
				item.hidden = !(okCategory && okQuery);
				if (!item.hidden) shown++;
			});
			if (empty) empty.hidden = shown !== 0;
		}

		buttons.forEach(function (button) {
			button.addEventListener('click', function () {
				buttons.forEach(function (b) { b.classList.remove('active'); b.setAttribute('aria-pressed', 'false'); });
				button.classList.add('active');
				button.setAttribute('aria-pressed', 'true');
				active = button.getAttribute('data-filter-button');
				apply();
			});
		});
		if (input) input.addEventListener('input', apply);
	});
})();
