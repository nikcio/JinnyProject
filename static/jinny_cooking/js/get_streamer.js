document.addEventListener('DOMContentLoaded', function(){
      const req = new XMLHttpRequest();
      //req.open("GET",'https://api.twitch.tv/helix/streams?user_id=159498717', true);
      req.open("GET",'https://api.twitch.tv/helix/streams?user_login=jinnytty', true);
      //req.open("GET",'https://api.twitch.tv/helix/streams?user_id=235634967', true); // TESTER Channel: yugwha0901
      req.setRequestHeader('Accept', 'application/vnd.twitchtv.v5+json');
      req.setRequestHeader('Client-ID', 'ijqkaxcdnlcq5j1xbndidaer460p7l');
      req.send();
      req.onload = function(){
          const json = JSON.parse(req.responseText);
          if(json.data.length != 0){
            //console.log(json);
            $('.live-now').addClass("show");
          }
      }
});