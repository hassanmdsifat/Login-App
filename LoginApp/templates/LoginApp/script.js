
            $(document).ready(function() {
             $('#customertable').DataTable( {
                    "processing": true,
                    "serverSide": true,
                    "ajax":"http://127.0.0.1:8000/api/customerapi/?format=json",
                    "columnDefs": [
                         {
                                "render": function ( data, type, row ) {
                                     console.log(row[0])

                                   let htmltext=`<button type="submit" class="btn btn-info mr-2"><a href="/edit/`+row[0]+`" style="text-decoration:none;color:white">Edit</a></button><button type="submit" class="btn btn-danger"><a href="/delete/`+row[0]+`" style="text-decoration:none;color:white">Delete</a></button>`;
                                   return htmltext;
                                },
                                "targets": 7
                         },
                         {
                          "render": function ( data, type, row ) {
                                     let yeararr=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
                                     //console.log(row[0])
                                     let date=new Date(data);
                                     let day=date.getDate();
                                     let month=yeararr[date.getMonth()-1];
                                     let year=date.getFullYear();
                                     let st=day;
                                     console.log(day);
                                     st+="-"+month+"-"+year;
                                   return st;
                                },
                                "targets": 5
                         },

                    ]

                } );
            } );