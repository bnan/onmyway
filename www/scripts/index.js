var thisButton,
    thisMenuItem,
    thisSubmenuItem,
    pieMenu = $('.radialnav'),
    menuItems  = $('.menu li'),
    submenuItems = $('.submenu'),
    submenuId = '';

function openMenu (thisButton) {
  if(!thisButton.hasClass('active'))
    thisButton.addClass('active');
  else
    $('.radialnav, .submenu').removeClass('active');
}

/* On click of the ellipsis */
$('.ellipsis').click(function (event) {
  event.preventDefault();

  openMenu($('.radialnav'));
});

menuItems.find('a').each(function (index) {
  thisMenuItem = $(this);

  thisMenuItem.hover(function () {
    // Hover over
    submenuId = menuItems.eq(index).attr('data-submenu');
    $('.submenu[data-submenuId="'+submenuId+'"]').addClass('active');
  }, function () {
    // Hover out
    // submenuItem.removeClass('active');
  });
});

submenuItems.find('a').hover(function () {
  console.log(1);
}, function () {
  console.log(0);
  submenuItems.hover(function () {
    console.log(2);
  }, function () {
    console.log(3);
  })
})
