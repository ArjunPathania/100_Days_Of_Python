// Animate navbar links on hover
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('mouseenter', () => {
      link.style.transform = 'scale(1.1)';
      link.style.boxShadow = '5px 5px 0 #000';
    });
    link.addEventListener('mouseleave', () => {
      link.style.transform = 'scale(1)';
      link.style.boxShadow = '2px 2px 0 #000';
    });
  });
  
  // Animate comic dots on load
  function floatDots() {
    document.querySelectorAll('.comic-dot').forEach(dot => {
      dot.animate([
        { transform: 'translateY(0px)' },
        { transform: 'translateY(-5px)' },
        { transform: 'translateY(0px)' }
      ], {
        duration: 1000 + Math.random() * 1000,
        iterations: Infinity
      });
    });
  }
  
  // Add bounce animation to buttons on click
  document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', () => {
      button.animate([
        { transform: 'scale(1)' },
        { transform: 'scale(1.2)' },
        { transform: 'scale(1)' }
      ], {
        duration: 300,
        easing: 'ease-out'
      });
    });
  });
  
  window.addEventListener('DOMContentLoaded', floatDots);
