document.addEventListener('DOMContentLoaded', () => {
  // Code Copy Button Functionality
  const copyButtons = document.querySelectorAll('.copy-btn');
  copyButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const codeBlock = btn.parentElement.nextElementSibling.querySelector('code');
      const text = codeBlock.innerText;
      
      navigator.clipboard.writeText(text).then(() => {
        const originalText = btn.innerText;
        btn.innerText = 'Copied!';
        setTimeout(() => {
          btn.innerText = originalText;
        }, 2000);
      });
    });
  });

  // Highlight active link in sidebar
  const currentUrl = window.location.href;
  const sidebarLinks = document.querySelectorAll('.sidebar ul li a');
  sidebarLinks.forEach(link => {
    if (currentUrl.includes(link.getAttribute('href'))) {
      link.classList.add('active');
    }
  });
});
