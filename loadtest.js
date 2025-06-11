/*
Load Testing menggunakan K6 untuk memanggil API secara bersamaan
*/

import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 133, // jumlah user
  duration: '1s', // waktu akses
};

export default function () {
  let res = http.get('http://localhost:5000/api/100');
  
  check(res, {
    'status was 200': (r) => r.status === 200,
    'response is not empty': (r) => r.body.length > 0,
  });

  sleep(1);
}