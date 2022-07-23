require 'html-proofer'

task :test do
  options = { 
    :allow_hash_href => true, 
    :ignore_empty_alt => true,
    :ignore_files => ["/assets/","/posts/"],
    :cache => { 
        :timeframe =>  '30d' 
    } ,
    :only_4xx => true,
    :ignore_status_codes => [429, 403, 400],
    :ignore_urls => ["/\#/"],
    :swap_urls => ["^/is310-computing-humanities/:/" ]
   }
  HTMLProofer.check_directory("_site").run
end

# htmlproofer _site --assume-extension --empty-alt-ignore --alt-ignore '/.*/' --file-ignore "/assets/,/posts/" --timeframe '30d' --only-4xx --http-status-ignore 429,403,400 --url-ignore "/\#/" --allow-hash-href --url-swap '^/is310-computing-humanities/:/'

# htmlproofer _site --assume-extension --ignore-empty-alt --ignore-files "/assets/,/posts/" --cache "{ \"timeframe\": { \"external\": \"30d\", \"internal\": \"30d\" } }" --only-4xx --ignore-status-codes 429,403,400 --ignore-urls "/\#/" --allow-hash-href --swap-urls '^/is310-computing-humanities/:/'