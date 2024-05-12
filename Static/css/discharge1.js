
document.addEventListener('DOMContentLoaded', function() {
  
  var roomChargeInput = document.getElementById('roomChargeInput');
  var doctorFeeInput = document.getElementById('doctorFeeInput');
  var medicineCostInput = document.getElementById('medicineCostInput');
  var otherChargeInput = document.getElementById('otherChargeInput');
  var totalInput = document.getElementById('totalInput');

  
  function calculateTotal() {
      var roomCharge = parseFloat(roomChargeInput.value) || 0;
      var doctorFee = parseFloat(doctorFeeInput.value) || 0;
      var medicineCost = parseFloat(medicineCostInput.value) || 0;
      var otherCharge = parseFloat(otherChargeInput.value) || 0;

      var total = roomCharge + doctorFee + medicineCost + otherCharge;
      totalInput.value = total.toFixed(2); 
  }

  
  roomChargeInput.addEventListener('input', calculateTotal);
  doctorFeeInput.addEventListener('input', calculateTotal);
  medicineCostInput.addEventListener('input', calculateTotal);
  otherChargeInput.addEventListener('input', calculateTotal);
});
